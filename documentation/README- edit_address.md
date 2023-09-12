### README- edit_address


#### Description-
- This API edits address details present in the *useraddresses* table.
- Data is passed to the API in JSON by frontend application.
- POST Method used.
- Assuming that pincode api is already applied.
- **The API will work only when the User is Logged in as we are passing token in Headers.**


#### API Url-
- http://127.0.0.1:8000/edit_address
- Headers: **KEY**- *Authorization*, **VALUE**- *Token 1bf4ba585defdedbc741bde94d0f20a8c4c6eb81*
- The token belonged to **gadia.aayush@gmail.com** login.


#### Test Data-
	{
		"data" :
		{
		"address_id" : 32934,
		"title" : "test_final_2_update",
	    "rec_name" : "aayush_test_2",
	    "pincode" : 123456,
	    "address" : "test_2",
	    "landmark" : "test_2",
	    "phone_no" : 1234567892,
	    "state_name" : "test_2",
	    "city_name" : "test_2",
	    "country_name" : "test2",
	    "is_primary" : "Y"
	}
	}


#### Output-
- Postman Output *(when properly data passed)*
![Postman Output](snap/output_postman_edit_address_1.png)

- Postman Output *(when improperly data passed)*
![Postman Output](snap/output_postman_edit_address_2.png)

- MySQL Output
![MySQL Output](snap/output_mysql_edit_address_1.png)


#### AUTHOR-
- **coded by AAYUSH GADIA** 
- **contact info: gadia.aayush@gmail.com**
