import argparse
import json
from typing import Text, Optional
import os
import logging

import questionary
from sqlalchemy import func
from sqlalchemy.orm import Session
from tqdm import tqdm

from rasa.cli.utils import print_error, print_success
from rasa.core.domain import Domain
from rasa.core.tracker_store import TrackerStore, InMemoryTrackerStore, SQLTrackerStore
from rasa.core.trackers import DialogueStateTracker
from rasa.core.utils import AvailableEndpoints

from rasax.community.database import ConversationStatistic
from rasax.community.services.event_service import EventService
import rasax.community.database.utils as db_utils
import rasax.community.sql_migrations as sql_migrations

logger = logging.getLogger(__name__)


def _create_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="Script to migrate from a Rasa Core tracker store to Rasa X.",
    )
    parser.add_argument("--max-trackers",
                        type=int,
                        default=None,
                        help="Number of trackers to migrate. "
                             "By default this migrates all trackers.")

    return parser


def _get_path_to_endpoints_config() -> Optional[Text]:
    return questionary.text(
        "Please provide the path to your endpoints "
        "configuration which "
        "specified the credentials for your old tracker store",
        default="endpoints.yml",
    ).ask()


def _migrate_tracker_store_to_rasa_x(endpoints_file: Text,
                                     max_number_of_trackers: Optional[int]) -> None:
    old_tracker_store = _get_old_tracker_store(endpoints_file)
    rasa_x_tracker_store = _get_rasa_x_tracker_store()

    # Disable warnings regarding not existing slots
    logging.getLogger("rasa.core.trackers").setLevel(logging.CRITICAL)

    if rasa_x_tracker_store.keys():
        should_migrate = questionary.confirm(
            "Found existing trackers in your Rasa X tracker store. Do you "
            "still want to migrate the new trackers?"
        )

        if not should_migrate:
            exit(1)

    db_session = db_utils.get_database_session(True, create_tables=True)
    sql_migrations.run_migrations(db_session)
    event_service = EventService(db_session)

    sender_ids = old_tracker_store.keys()

    if max_number_of_trackers:
        sender_ids = sender_ids[:max_number_of_trackers]

    print_success("Start migrating {} trackers.".format(len(sender_ids)))

    nr_skipped_trackers = 0

    for sender_id in tqdm(sender_ids):
        if rasa_x_tracker_store.retrieve(sender_id):
            nr_skipped_trackers += 1
            logging.debug("Tracker for sender '{}' already exists. Skipping the "
                          "migration for it.".format(sender_id))
        else:
            tracker = old_tracker_store.retrieve(sender_id)

            # Migrate tracker store to new tracker store format
            rasa_x_tracker_store.save(tracker)

            # Replay events of tracker
            _replay_tracker_events(tracker, event_service)

    # Set latest event id so that the `SQLiteEventConsumer` only consumes not already
    # migrated events
    set_latest_event_id(db_session, rasa_x_tracker_store)

    print_success("Finished migrating trackers ({} were skipped since they were "
                  "already migrated).".format(nr_skipped_trackers))


def _get_old_tracker_store(endpoints_file: Text) -> TrackerStore:
    if (
        not endpoints_file
        or not os.path.isfile(endpoints_file)
        or not os.path.exists(endpoints_file)
    ):
        print_error(
            "File '{}' was not found. Please specify a valid file with "
            "'--endpoints <file>'.".format(endpoints_file)
        )
        exit(1)

    endpoints = AvailableEndpoints.read_endpoints(endpoints_file)

    tracker_store = TrackerStore.find_tracker_store(
        Domain.empty(), endpoints.tracker_store
    )

    if not tracker_store or isinstance(tracker_store, InMemoryTrackerStore):
        print_error(
            "No valid tracker store config given. Please provide a valid "
            "tracker store configuration as it is described here: "
            "https://rasa.com/docs/core/0.14.4/tracker_stores/"
        )
        exit(1)

    return tracker_store


def _get_rasa_x_tracker_store() -> SQLTrackerStore:
    return SQLTrackerStore(Domain.empty(), db="tracker.db")


def _replay_tracker_events(tracker: DialogueStateTracker,
                           event_service: EventService) -> None:
    """Migrates the `events`, `logs`, `sessions` collections."""

    for event in tracker.events:
        event_dict = event.as_dict()
        # add sender id to event
        event_dict["sender_id"] = tracker.sender_id
        stringified_event = json.dumps(event_dict)
        # Update events + most of conversations metadata
        _ = event_service.save_event(stringified_event)


def set_latest_event_id(db_session: Session, rasa_x_tracker_store: SQLTrackerStore
                        ) -> None:
    (max_event_id,) = rasa_x_tracker_store.session.query(
        func.max(SQLTrackerStore.SQLEvent.id)).first()

    print(max_event_id)
    existing = db_session.query(ConversationStatistic).first()
    existing.latest_event_id = max_event_id

    db_session.commit()

    logging.debug("Set max event id to {}.".format(max_event_id))


if __name__ == "__main__":
    parser = _create_argument_parser()
    args = parser.parse_args()

    print_success(
        "Welcome to Rasa X 🚀 \n\nThis script will migrate your old tracker "
        "store to the new SQL based Rasa X tracker store."
    )
    print_success("Let's start!\n")

    path_to_endpoints_file = _get_path_to_endpoints_config()
    _migrate_tracker_store_to_rasa_x(path_to_endpoints_file, args.max_trackers)