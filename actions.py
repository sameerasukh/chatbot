from __future__ import division
from __future__ import unicode_literals
from rasa_sdk import Action
#from rasa_sdk.action import Action
from rasa_sdk.events import SlotSet
#import mysql.connector


'''class ActionMessage(Action):
	def name(self):
		return "action_message"

	def run(self,dispatcher,tracker,domain):
		response="hey here is your message"
		dispatcher.utter_message(response)
		return []'''

class ActionCustom(Action):
    def name(self):
        return "action_custom"
    
    def run(self,dispatcher,tracker,domain):
        dispatcher.utter_template("utter_message",tracker)
     