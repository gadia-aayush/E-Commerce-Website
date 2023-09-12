### README- generate_razorpayid


#### Description-
- This API takes **Order Id** & the **Amount of transaction** as Input.
- It returns **Razorpay Id** as an Output.
- This **Razorpay Id** is passed to the **Razorpay JS Checkout form.**
- This API uses **Razorpay's Orders API.**
- Data is passed to the API in JSON by frontend application.
- POST Method used.


#### API Url-
- http://127.0.0.1:8000/get_razorpayid


#### Test Data-
	{
	    "data" :
	    {
	        "ref_id" : 1,
	        "amount" : 100
	    }
	}


#### Output-
- Postman Output
![Postman Output](snap/output_postman_generate_razorpayid.png)


#### References-
- https://github.com/razorpay/razorpay-python **(razorpay documentation for python)**
- https://docs.razorpay.com/docs/checkout-form *(checkout form)*
- https://checkout.razorpay.com/v1/checkout.js *(checkout javascript)*
- **The CSV file of Live RazorPay & Test RazorPay API Credentials** is in app directory.
- Razorpay PG Flowchart-
![RP Flowchart](razorpay_pg_flowchart.png)


#### AUTHOR-
- **coded by AAYUSH GADIA** 
- **contact info: gadia.aayush@gmail.com**

