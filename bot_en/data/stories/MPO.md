

## decrease_MPO affirm path
* greet
  - utter_greet
* reduce_MPO
 - utter_decrease_MPO
 - utter_ask_satisfication
* affirm
 - utter_affirm
* thanks
 - utter_happy

## decrease_MPO deny first path
* greet
  - utter_greet
* reduce_MPO
 - utter_decrease_MPO
 - utter_ask_satisfication
* deny
 - utter_decrease_general_gain
 - utter_ask_satisfication
* affirm
 - utter_affirm


## decrease_brightness deny second path
* greet
  - utter_greet
* reduce_bright
 - utter_reduce_bright
 - utter_ask_satisfication
* deny
 - utter_decrease_MPO
 - utter_ask_satisfication
* deny
 - utter_troubleshooting
* thanks
  - utter_make_note

## ask_what_is_MPO path
* greet
  - utter_greet
* reduce_MPO
 - utter_reduce_MPO
 - utter_ask_satisfication
* what_is_MPO
 - utter_this_is_MPO