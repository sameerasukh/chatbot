## happy_path1
* greetings
  - utter_greetings
  - utter_what_treatment
* treatment
  - utter_howlong_suffer
* answer_suffer_for
  - utter_ask_reports
* answer_reports
  - utter_thank_for_reports
  - utter_ask_contact_details
* answer_contact_details
  - utter_thanks_for_contact_details
  - utter_time
* answer_time
  - utter_you_receive_call
* bye
  - utter_bye

## happy_path2
* treatment
  - utter_howlong_suffer
* answer_suffer_for
  - utter_ask_reports
* answer_reports
  - utter_thank_for_reports
  - utter_ask_contact_details
* answer_contact_details
  - utter_thanks_for_contact_details
  - utter_time
* answer_time
  - utter_you_receive_call
* bye
  - utter_bye

## happy_path3
* treatment
  - utter_howlong_suffer
* answer_contact_details
  - utter_thanks_for_contact_details
  - utter_time
* answer_time
  - utter_you_receive_call
* bye
  - utter_bye

## path4
* treatment
  - utter_howlong_suffer
* answer_contact_details
  - utter_thanks_for_contact_details
  - utter_time
* answer_time
  - utter_you_receive_call

## cost
* ask_cost
  - action_check_treatment
* ask_rationale
  - action_rationale_gst
* comment_rationale
  - utter_ask_reports
* answer_reports
  - utter_thank_for_reports
  - utter_ask_contact_details
* answer_contact_details
  - utter_thanks_for_contact_details
  - utter_time
* answer_time
  - utter_you_receive_call
* bye
  - utter_bye  


- action_check_treatment
- action_rationale_gst

## happy_path3
* treatment
  - utter_howlong_suffer
* answer_contact_details
  - utter_thanks_for_contact_details
  - utter_time
* answer_time
  - utter_you_receive_call
* bye
  - utter_bye

## path4
* treatment
  - utter_howlong_suffer
* answer_contact_details
  - utter_thanks_for_contact_details
  - utter_time
* answer_time
  - utter_you_receive_call


  from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RegexInterpreter
from rasa_core.interpreter import RasaNLUInterpreter
nlu_interpreter = RasaNLUInterpreter('./models/nlu')
agent = Agent.load('./models/core', interpreter = nlu_interpreter)
input_channel = SlackInput(
        slack_token="xoxb-752604530980-752610042244-hV6xy3XmrqKYrfVrUNg2wHac"
        # this is the `bot_user_o_auth_access_token`
        #slack_channel="YOUR_SLACK_CHANNEL"
            # the name of your channel to which the bot posts (optional)
    )
serve_forever=True
s = agent.handle_channels([input_channel], 5004, serve_forever=True)
