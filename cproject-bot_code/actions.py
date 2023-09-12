from collections import Counter
from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet 

import json, requests, random


######################################

class ActionReset(Action):  #Since it is a Trigger and not Form Action so we wrote Action in the parenthesis

    def name(self) -> Text:
        return "action_reset"


    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return_slots = []
        for slot in tracker.slots:
            if slot != "foo":
                return_slots.append(SlotSet(slot, None))
        return return_slots


        #tracker.slots returns the slots keys which are in the bot
        #then we will check each slot key's to make sure that it is != "foo"
        #if != "foo" then we will set the value of slot as None and we will append it to the return_slots
        #finally, we will return return_slots
    

######################################

class DonationQueries(FormAction):

    def name(self) -> Text:
        return 'donation_queries_form'


    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["Donation"]


    def validate_Donation(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
        if value:
            with open ('data/general-queries.json', 'r') as f:
                data = json.load(f)

            query_ans = data["donation"][value]
            print (query_ans)                 
            dispatcher.utter_message(query_ans)
            return {"Donation": value}

        else:
            dispatcher.utter_template("utter_wrong", tracker)
        return {"Donation": None}


    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {"Donation": self.from_entity(entity="Donation")}  #this might be incorrect


    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        
        return_slots = []
        for slot in ["Donation"]:
            if slot != "foo":
                return_slots.append(SlotSet(slot, None))

        return return_slots


######################################

class DeliveryQueries(FormAction):

    def name(self) -> Text:
        return 'delivery_queries_form'


    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["Delivery"]


    def validate_Delivery(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
        if value:
            with open ('data/general-queries.json', 'r') as f:
                data = json.load(f)

            query_ans = data["delivery"][value]                    
            dispatcher.utter_message(query_ans)
            return {"Delivery": value}

        else:
            dispatcher.utter_template("utter_wrong", tracker)
        return {"Delivery": None}


    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {"Delivery": self.from_entity(entity="Delivery")}  #this might be incorrect


    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        
        return_slots = []
        for slot in ["Delivery"]:
            if slot != "foo":
                return_slots.append(SlotSet(slot, None))

        return return_slots


######################################

class GeneralQueries(FormAction):

    def name(self) -> Text:
        return 'general_queries_form'


    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["General"]


    def validate_General(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
        if value:
            with open ('data/general-queries.json', 'r') as f:
                data = json.load(f)

            query_ans = data["general"][value]                    
            dispatcher.utter_message(query_ans)
            return {"General": value}

        else:
            dispatcher.utter_template("utter_wrong", tracker)
        return {"General": None}


    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {"General": self.from_entity(entity="General")}  #this might be incorrect


    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        
        return_slots = []
        for slot in ["General"]:
            if slot != "foo":
                return_slots.append(SlotSet(slot, None))

        return return_slots


######################################

class PaymentQueries(FormAction):

    def name(self) -> Text:
        return 'payment_queries_form'


    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["Payment"]


    def validate_Payment(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
        if value:
            with open ('data/general-queries.json', 'r') as f:
                data = json.load(f)

            print (value)
            query_ans = data["payment"][value]                    
            dispatcher.utter_message(query_ans)
            print (query_ans)
            return {"Payment": value}

        else:
            dispatcher.utter_template("utter_wrong", tracker)
        return {"Payment": None}


    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {"Payment": self.from_entity(entity="Payment")}  #this might be incorrect


    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        
        return_slots = []
        for slot in ["Payment"]:
            if slot != "foo":
                return_slots.append(SlotSet(slot, None))

        return return_slots


######################################