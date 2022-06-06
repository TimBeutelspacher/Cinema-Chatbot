# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from posixpath import dirname
from typing import Any, Text, Dict, List

from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pathlib

# Load list of available movies
movies = pathlib.Path("data/movies.txt").read_text().split("\n")

# Set movie slot 
class ActionReceiveMovie(Action):

    def name(self) -> Text:
        return "action_receive_movie"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        text = tracker.latest_message['text']

        # validate given movie

        dispatcher.utter_message(text=f"{text}, good choice!")
        return [SlotSet("movie_name", text)]

# Set amount slot 
class ActionReceiveAmount(Action):

    def name(self) -> Text:
        return "action_receive_amount"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        text = tracker.latest_message['text']
        dispatcher.utter_message(text=f"{text} ticket(s), ok.")
        return [SlotSet("no_of_tickets", text)]

# Set date slot 
class ActionReceiveDate(Action):

    def name(self) -> Text:
        return "action_receive_date"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        text = tracker.latest_message['text']
        
        # validate given date

        dispatcher.utter_message(text=f"{text} registered.")
        return [SlotSet("planned_date", text)]

# Set time slot 
class ActionReceiveTime(Action):

    def name(self) -> Text:
        return "action_receive_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        text = tracker.latest_message['text']
        
        # validate given time

        dispatcher.utter_message(text=f"{text} registered.")
        return [SlotSet("planned_time", text)]

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
        planned_time = tracker.get_slot("no_of_tplanned_timeickets")

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
            dispatcher.utter_message(text=f"As you wished, {amount} tickets for the movie {movie_name} on {planned_date} {planned_time} are booked successfully.")
        
        return []


## Help functions

# funtion to check if all the necessary slots are filled, to call the booking function