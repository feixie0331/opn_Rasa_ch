## decrease_MPO affirm path
* greet
  - utter_greet
* reduce_MPO
 - utter_decrease_MPO
* affirm
 - utter_affirm
* thanks
 - utter_thanks

## decrease_MPO deny first path
* greet
  - utter_greet
* reduce_MPO
 - utter_decrease_MPO
* deny
 - utter_decrease_general_gain
* affirm
 - utter_affirm

## decrease_brightness deny second path
* greet
  - utter_greet
* reduce_bright
 - utter_reduce_bright
* deny
 - utter_decrease_MPO
* deny
 - utter_troubleshooting
* thanks
  - utter_make_note

## ask_what_is_MPO path
* greet
  - utter_greet
* reduce_MPO
 - utter_reduce_MPO
* what_is_MPO
 - utter_this_is_MPO
