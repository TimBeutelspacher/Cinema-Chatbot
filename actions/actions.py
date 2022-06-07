# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from posixpath import dirname
from typing import Any, Text, Dict, List

from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
import pathlib

# Load list of available movies
AVAILABLE_MOVIES = pathlib.Path("data/available_movies.txt").read_text().split("\n")
AVAILABLE_DATES = pathlib.Path("data/available_dates.txt").read_text().split("\n")
AVAILABLE_TIMES = pathlib.Path("data/available_times.txt").read_text().split("\n")
AVAILABLE_AMOUNTS = pathlib.Path("data/available_amounts.txt").read_text().split("\n")

# validate user information
class ValidateBookingForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_bookingForm"

    def validate_movie_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `movie_name` value."""

        if slot_value.lower() not in AVAILABLE_MOVIES:
            dispatcher.utter_message(text=f"We don't have this movie in our cinema. Please choose one of the following: \n {AVAILABLE_MOVIES}")
            return {"movie_name": None}
        dispatcher.utter_message(text=f"{slot_value} is a great choice!.")
        return {"movie_name": slot_value}

    def validate_planned_date(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `planned_date` value."""

        if slot_value.lower() not in AVAILABLE_DATES:
            dispatcher.utter_message(text=f"This movie is only shown on the following dates: \n {AVAILABLE_DATES}")
            return {"planned_date": None}
        dispatcher.utter_message(text=f"{slot_value} will be a good day!")
        return {"planned_date": slot_value}

    def validate_planned_time(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `planned_time` value."""

        if slot_value.lower() not in AVAILABLE_TIMES:
            dispatcher.utter_message(text=f"This movie is only on the following times: \n {AVAILABLE_TIMES}")
            return {"planned_time": None}
        dispatcher.utter_message(text=f"{slot_value} is movie time!")
        return {"planned_time": slot_value}

    def validate_no_of_tickets(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `no_of_tickets` value."""

        if slot_value.lower() not in AVAILABLE_AMOUNTS:
            dispatcher.utter_message(text=f"You can only book up to 10 tickets at once.")
            return {"no_of_tickets": None}
        dispatcher.utter_message(text=f"{slot_value} ticket(s) registered.")
        return {"no_of_tickets": slot_value}

# Book ticket(s) with provided information
class ActionBookTickets(Action):

    def name(self) -> Text:
        return "action_book_tickets"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        text = tracker.latest_message['text']

        # load the provided slot-data
        amount = tracker.get_slot("no_of_tickets")
        movie_name = tracker.get_slot("movie_name")
        planned_date = tracker.get_slot("planned_date")
        planned_time = tracker.get_slot("planned_time")

        if not amount:
            dispatcher.utter_message(text="You need to enter the number of tickets first!")
        elif not movie_name:
            dispatcher.utter_message(text="You need to enter the movie first!")
        elif not planned_date:
            dispatcher.utter_message(text="You need to enter a date first!")
        elif not planned_time:
            dispatcher.utter_message(text="You need to enter a time first!")
        else:
            # in reallife practice --> API-call to book the tickets in internal system
            dispatcher.utter_message(text=f"As you wished, {amount} ticket(s) for the movie {movie_name} on {planned_date} {planned_time} booked successfully.")
        
        return []


## Help functions

# funtion to check if all the necessary slots are filled, to call the booking function