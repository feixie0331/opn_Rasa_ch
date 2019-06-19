## focused affirm path
* focused
  - utter_focused
* affirm
  - utter_affirm
  
## focused deny path
* focused
  - utter_focused
* deny
  - utter_deny

## reduce noise path affirm
* reduce_noise
  - utter_reduce_noise
* affirm
  - utter_affirm

## reduce noise path deny
* reduce_noise
  - utter_reduce_noise
* deny
  - utter_deny 

## reduce noise explain path affirm
* reduce_noise
  - utter_reduce_noise
* what_focused
  - utter_focused_change
* affirm
  - utter_affirm

## reduce noise explain path deny
* reduce_noise
  - utter_reduce_noise
* what_focused
  - utter_focused_change
* deny
  - utter_deny