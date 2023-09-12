### README- book_notify


#### Description-
- This API inserts user's email, user's id & the book details- title & isbn to *booknotify* table.
- Assuming that- 
  If a user is logged in then the email address section is auto-fetched & the user just has to submit.
- **The API will work only when the User is Logged in as we are passing token in Headers.**
- Data is passed to the API in JSON by frontend application.
- POST Method used.


#### API Url-
- http://127.0.0.1:8000/notify_me
- Headers: **KEY**- *Authorization*, **VALUE**- *Token 1bf4ba585defdedbc741bde94d0f20a8c4c6eb81*
- The token belonged to **gadia.aayush@gmail.com** login.


#### Test Data-
	{
		"data" :
		{
		"slug" : "clarks-tables-science-data-book"
	}
	}


#### Output-
- Postman Output *(when successfully added)*
![Postman Output](snap/output_postman_book_notify_1.png)

- Postman Output *(when error)*
![Postman Output](snap/output_postman_book_notify_2.png)

- MySQL Output
![MySQL Output](snap/output_mysql_book_notify.png)


#### AUTHOR-
- **coded by AAYUSH GADIA** 
- **contact info: gadia.aayush@gmail.com**
