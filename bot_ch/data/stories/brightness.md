## increase_brightness affirm path
* increase_bright
  - utter_increase_bright
* affirm
  - slot{"brightness" : "increase"}
  - action_note_adjust
  - utter_affirm
* thanks
  - utter_thanks
* goodbye
  - utter_goodbye

## increase_brightness deny_first path
* increase_bright
  - utter_increase_bright
* deny
  - utter_increase_MPO
* affirm
  - slot{"MPO" : "increase"}
  - action_note_adjust
  - utter_affirm
* thanks
  - utter_thanks
* goodbye
  - utter_goodbye

## increase_brightness deny_second path
* increase_bright
  - utter_increase_bright
* deny
  - utter_increase_MPO
* deny
  - action_leave_note
  - utter_troubleshooting
* thanks
  - utter_thanks
* goodbye
  - utter_goodbye

## decrease_brightness affirm path
* reduce_bright
 - utter_reduce_bright
* affirm
 - slot{"brightness" : "decrease"}
 - utter_affirm
 - action_note_adjust
* thanks
 - utter_thanks
* goodbye
  - utter_goodbye

## decrease_brightness deny first path
* reduce_bright
 - utter_reduce_bright
* deny
 - utter_decrease_MPO
* affirm
 - slot{"MPO" : "decrease"}
 - utter_affirm
 - action_note_adjust
* thanks
 - utter_thanks
* goodbye
  - utter_goodbye

## decrease_brightness deny second path
* reduce_bright
 - utter_reduce_bright
* deny
 - utter_decrease_MPO
* deny
 - action_leave_note
 - utter_troubleshooting
* thanks
  - utter_thanks

## ask_what_is_brightness path
* reduce_bright
 - utter_reduce_bright
* what_is_bright
 - utter_this_is_bright
