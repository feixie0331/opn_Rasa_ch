## increase_soft_gain affirm path
* increase_soft_gain
  - utter_increase_soft_gain
* affirm
  - utter_affirm
* thanks
  - utter_thanks

## increase_soft_gain deny_first path
* increase_soft_gain
  - utter_increase_soft_gain
* deny
  - utter_reduce_bright
* affirm
  - utter_affirm
* thanks
  - utter_thanks

## increase_soft_gain deny_second path
* increase_soft_gain
  - utter_increase_soft_gain
* deny
  - utter_reduce_bright
* deny
  - utter_troubleshooting
* thanks
  - utter_thanks

## decrease_soft_gain affirm path
* decrease_soft_gain
 - utter_decrease_soft_gain
* affirm
 - utter_affirm
* thanks
 - utter_thanks

## decrease_soft_gain deny first path
* decrease_soft_gain
 - utter_decrease_soft_gain
* deny
 - utter_reduce_noise
* affirm
 - utter_affirm


## decrease_soft_gain deny second path
* decrease_soft_gain
 - utter_decrease_soft_gain
* deny
 - utter_reduce_noise
* deny
 - utter_frontal_focus
* thanks
  - utter_make_note

## ask_what_is_soft_gain increase_path
* increase_soft_gain
  - utter_increase_soft_gain
* what_is_soft_gain
 - utter_this_is_soft_gain
* affirm
  - utter_affirm
* thanks
  - utter_thanks

## ask_what_is_soft_gain decrease_path
* decrease_soft_gain
  - utter_decrease_soft_gain
* what_is_soft_gain
 - utter_this_is_soft_gain
* affirm
  - utter_affirm
* thanks
  - utter_thanks

 