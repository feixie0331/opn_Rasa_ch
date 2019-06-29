# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
import logging
from typing import Dict, Text, Any, List, Union, Optional
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction


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


class ProgramForm(FormAction):
    def name(self):
        return "program_form"
    
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return["satisfaction", "configuration"]

    @staticmethod
    def desciptors_db() -> List[Text]:
        """Database of supported settings"""

        return [
            "crisp",
            "lively",
            "natural",
            "focused",
            "indian",
            "occlusion",
            "ambience",
            "speech",
            "brightness",
            "intensity",
            "noise",
        ]


    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "configuration": self.from_entity(entity="feature", not_intent="chitchat"),
#            "num_people": [
#                self.from_entity(
#                    entity="num_people", intent=["inform", "request_restaurant"]
#                ),
#                self.from_entity(entity="number"),
#            ],
            "satisfaction": [
                self.from_intent(intent="affirm", value=True),
                self.from_intent(intent="deny", value=False),
            ],
#            "preferences": [
#                self.from_intent(intent="deny", value="no additional preferences"),
#                self.from_text(not_intent="affirm"),
#            ],
#            "feedback": [self.from_entity(entity="feedback"), self.from_text()],
        }

    def submit(self):
        dispatcher.utter_template('utter_affirm')
        return[]