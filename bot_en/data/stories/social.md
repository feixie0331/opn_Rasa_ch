## greet path enhance speech
* greet
  - action_fetch_labels
  - slot{"label":"meeting room work meeting"}
  - utter_enhance_speech

## greet path reduce
* greet
  - action_fetch_labels
  - slot{"label":"lecture listening to speech"}
  - utter_focused

## thanks path
* thanks
  - utter_thanks

## report path
* report_problem
  - utter_deny

## say goodbye
* goodbye
  - utter_goodbye

## test path
* test
  - action_fetch_UserId
  - slot{"userid" : "basic"}
  - action_hello_world
