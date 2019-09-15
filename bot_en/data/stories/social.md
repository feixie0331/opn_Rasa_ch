## deny path enhance speech
* deny
  - action_fetch_labels
  - slot{"label":"meeting room work meeting"}
  - utter_enhance_speech

## deny path_focus
* deny
  - action_fetch_labels
  - slot{"label":"lecture listening to speech"}
  - utter_focused


## thanks path
* thanks
  - utter_thanks


## say goodbye
* goodbye
  - utter_goodbye

## test path
* test
  - action_fetch_UserId
  - slot{"userid" : "basic"}
  - action_hello_world
