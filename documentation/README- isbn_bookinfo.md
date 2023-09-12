### README- isbn_bookinfo


#### Description-
- This API fetches the book details by isbn.
- It first searches for **our database** for the isbn, if it is not found then it hits the **googlebooks api.**
- Data is passed to the API in JSON.
- POST Method used.


#### API Url-
- http://127.0.0.1:8000/get_bookinfo


#### Test Data-

	{ "data" :
	  {
	  	"isbn" : 9789610104841
	  	}
	}


#### Output-
- Postman Output (by local db)
![Postman Output](snap/output_postman_isbn_bookinfo_mp.png)

- Postman Output (by google-api)
![MySQL Output](snap/output_postman_isbn_bookinfo_googleapi.png)


#### References-
- **isbn : 9789610104841 (will fetch from google api)**
- **isbn : 9788186423271 (will fetch from db)**


#### AUTHOR-
- **coded by AAYUSH GADIA** 
- **contact info: gadia.aayush@gmail.com**
