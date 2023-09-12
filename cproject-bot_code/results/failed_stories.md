## happy path 1
* greet: hello there!
    - utter_greet
* mood_great: amazing   <!-- predicted: bot_challenge: amazing -->
    - utter_happy   <!-- predicted: utter_iamabot -->


## happy path 2
* greet: hello there!
    - utter_greet
* mood_great: amazing   <!-- predicted: bot_challenge: amazing -->
    - utter_happy   <!-- predicted: utter_iamabot -->
* goodbye: bye-bye!
    - utter_goodbye


## sad path 1
* greet: hello
    - utter_greet
* mood_unhappy: not good   <!-- predicted: greet: not good -->
    - utter_cheer_up   <!-- predicted: utter_greet -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* affirm: yes   <!-- predicted: goodbye: yes -->
    - utter_happy   <!-- predicted: utter_goodbye -->


## sad path 2
* greet: hello
    - utter_greet
* mood_unhappy: not good   <!-- predicted: greet: not good -->
    - utter_cheer_up   <!-- predicted: utter_greet -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: not really   <!-- predicted: greet: not really -->
    - utter_goodbye   <!-- predicted: utter_greet -->


## sad path 3
* greet: hi
    - utter_greet
* mood_unhappy: very terrible   <!-- predicted: general: very terrible -->
    - utter_cheer_up   <!-- predicted: general_queries_form -->
    - utter_did_that_help   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: general_queries_form -->
* deny: no   <!-- predicted: greet: no -->
    - utter_goodbye   <!-- predicted: action_listen -->


