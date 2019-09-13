## increase_soft_gain affirm path
* increase_soft_gain
  - utter_increase_soft_gain
  - utter_ask_satisfication
* affirm
  - utter_affirm
* thanks
  - utter_happy

## increase_soft_gain deny_first path
* increase_soft_gain
  - utter_increase_soft_gain
  - utter_ask_satisfication
* deny
  - utter_reduce_bright
  - utter_ask_satisfication
* affirm
  - utter_affirm
* thanks
  - utter_happy

## increase_soft_gain deny_second path
* increase_soft_gain
  - utter_increase_soft_gain
  - utter_ask_satisfication
* deny
  - utter_reduce_bright
  - utter_ask_satisfication
* deny
  - utter_troubleshooting
* thanks
  - utter_make_note

## decrease_soft_gain affirm path
* decrease_soft_gain
 - utter_decrease_soft_gain
 - utter_ask_satisfication
* affirm
 - utter_affirm
* thanks
 - utter_happy

## decrease_soft_gain deny first path
* decrease_soft_gain
 - utter_decrease_soft_gain
 - utter_ask_satisfication
* deny
 - utter_reduce_noise
 - utter_ask_satisfication
* affirm
 - utter_affirm


## decrease_soft_gain deny second path
* decrease_soft_gain
 - utter_decrease_soft_gain
 - utter_ask_satisfication
* deny
 - utter_reduce_noise
 - utter_ask_satisfication
* deny
 - utter_frontal_focus
* thanks
  - utter_make_note

## ask_what_is_soft_gain path
* decrease_soft_gain
 - utter_decrease_soft_gain
 - utter_ask_satisfication
* what_is_soft_gain
 - utter_this_is_soft_gain
 