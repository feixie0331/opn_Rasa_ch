## greet path
* greet
  - utter_greet
  - utter_ask_satisfication

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

## Generated Story 8511563781940770780
* report_problem
    - utter_deny
* enhance_ambience
    - utter_enhance_ambience
* what_lively{"features": "lively"}
    - utter_lively_change
* deny
    - rewind
* affirm
    - utter_anything_else
* satisfied
    - utter_affirm
* thanks
    - utter_thanks
* goodbye
    - utter_goodbye