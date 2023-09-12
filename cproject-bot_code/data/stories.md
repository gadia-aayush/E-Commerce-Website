## say goodbye
* goodbye
  - utter_goodbye


## say greet
* greet
  - utter_greet


## Donation
* donation
  - donation_queries_form
  - form{"name": "donation_queries_form"}
  - slot{"requested_slot":"Donation"}
* inform{"Donation":"How can I donate books?"}
  - donation_queries_form
  - slot{"Donation":"How can I donate books?"}
  - form{"name":null}
  - slot{"requested_slot":null}


## Delivery
* delivery
  - delivery_queries_form
  - form{"name": "delivery_queries_form"}
  - slot{"requested_slot":"Delivery"}
* inform{"Delivery":"In how many days my books will be delivered to the address i mentioned in book request."}
  - delivery_queries_form
  - slot{"Delivery":"In how many days my books will be delivered to the address i mentioned in book request."}
  - form{"name":null}
  - slot{"requested_slot":null}


## Payment
* payment
  - payment_queries_form
  - form{"name": "payment_queries_form"}
  - slot{"requested_slot":"Payment"}
* inform{"Payment":"Do I have to pay for the books I requested ?"}
  - payment_queries_form
  - slot{"Payment":"Do I have to pay for the books I requested ?"}
  - form{"name":null}
  - slot{"requested_slot":null}


## General
* general
  - general_queries_form
  - form{"name": "general_queries_form"}
  - slot{"requested_slot":"General"}
* inform{"General":"I am not able to add the  books in my cart."}
  - general_queries_form
  - slot{"General":"I am not able to add the  books in my cart."}
  - form{"name":null}
  - slot{"requested_slot":null}


## say iambot
* bot_challenge
  - utter_iamabot


## reset
* reset
  - action_reset


## respond insult
* insult
  - utter_respond_insult


## respond out_of_scope qns 
* out_of_scope
  - utter_cannot_help
  - utter_wrong

