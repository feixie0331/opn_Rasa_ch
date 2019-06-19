# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
import logging
from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

logger = logging.getLogger(__name__)

#
#
class ActionHelloWorld(Action):
    def name(self):
        return "action_hello_world"
#
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
        dispatcher.utter_message("Hello World!")
#
        return []

class FetchUserIdAction(Action):
    def name(self):
        return "action_fetch_UserId"
    def run(self, dispatcher, tracker, domain):
        sender_id = tracker.sender_id
        dispatcher.utter_message("userid{}".format(sender_id))
        return [SlotSet("userid", sender_id)]

class ActionLeaveNote(Action):
    def name(self):
        return "action_leave_note"
    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        with open("Output.txt", "w") as text_file:
            text_file.write("New dom needed")
        dispatcher.utter_message("HHHHH")
        # utter submit template
        dispatcher.utter_template("utter_make_note", tracker)
        return []

