## increase_brightness affirm path
* increase_bright
  - utter_increase_bright
  - utter_ask_satisfication
* affirm
  - utter_affirm
* thanks
  - utter_happy

## increase_brightness deny_first path
* increase_bright
  - utter_increase_bright
  - utter_ask_satisfication
* deny
  - utter_increase_MPO
  - utter_ask_satisfication
* affirm
  - utter_affirm
* thanks
  - utter_happy

## increase_brightness deny_second path
* increase_bright
  - utter_increase_bright
  - utter_ask_satisfication
* deny
  - utter_increase_MPO
  - utter_ask_satisfication
* deny
  - utter_troubleshooting
* thanks
  - utter_make_note

## decrease_brightness affirm path
* reduce_bright
 - utter_reduce_bright
 - utter_ask_satisfication
* affirm
 - utter_affirm
* thanks
 - utter_happy

## decrease_brightness deny first path
* reduce_bright
 - utter_reduce_bright
 - utter_ask_satisfication
* deny
 - utter_decrease_MPO
 - utter_ask_satisfication
* affirm
 - utter_affirm


## decrease_brightness deny second path
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

## ask_what_is_brightness path
* reduce_bright
 - utter_reduce_bright
 - utter_ask_satisfication
* what_is_bright
 - utter_this_is_bright
 