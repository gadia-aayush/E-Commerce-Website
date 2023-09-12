### README- cancel_order


#### Description-
- This API cancels the order & changes the value of following attributes- *status, qty, is_soldout/ is_out_of_stack  & u_date* present in *orders, bookinventory & books table.*
- POST Method used.
- User token is passed to the API in headers.
- **The API will work only when the User is Logged in as we are passing token in Headers.**
- **Assumed-**
   - for example, in an order more than 1 qty of books are ordered for 1 particular book_id then for each book separate row is inserted in the order_books table.


#### API Url-
- http://127.0.0.1:8000/cancel_order
- Headers: **KEY**- *Authorization*, **VALUE**- *Token 1bf4ba585defdedbc741bde94d0f20a8c4c6eb81*
- The token belonged to **gadia.aayush@gmail.com** login.


#### Test Data-
	{
		"data" :
		{
			"order_id" : 1
		}
	}


#### Output-
- Postman Output *(when cancellation requested)*
![Postman Output](snap/output_postman_cancel_order_1.png)

- Postman Output *(when cancellation requested on order whose status != 0)*
![Postman Output](snap/output_postman_cancel_order_2.png)


#### AUTHOR-
- **coded by AAYUSH GADIA** 
- **contact info: gadia.aayush@gmail.com**
