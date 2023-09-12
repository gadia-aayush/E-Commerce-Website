#### README- myauth


##### API Name, Description, it's EndPoints, TestCases, ScreenShots-

- *API EndPoints-*
	- *Login URL- http://127.0.0.1:8000/myauth/login/ (POST API)*
	- *Logout URL- http://127.0.0.1:8000/myauth/logout/ (GET API)*
	   - *(Key, Value) passed in Headers :: (Authorization, Token ccacf07ed29370f863ad74699359819ebca3a35a)*
	   - *The above passed token is just an example.*
	- *SignUp URL- http://127.0.0.1:8000/myauth/signup/ (POST API)*
	- *GetToken URL- http://127.0.0.1:8000/myauth/get-token/ (POST API)*
		- *(Key, Value) passed in Form-data of Body :: (phone : 8334827095, password : Aayush@2020)*
		- *The above passed value is just an example.*

- *Description-*
	- *Login is done using HTML Templates, because their is CSRF Validation by Django so it can't be developed without rendering a Page. Similarly SignUp is done*
	- *For, security issues whenever a user will login, then on passing the username & password of the user to the *GetToken URL Endpoint, token would be returned. Using this token we could restrict all the functionality of the Application like **Search, Marking Spam, Logout** (this was also asked, that nothing would be public)*
	- *When the Logout URL Endpoint is hit, then the user whose token was authenticated, that user token is deleted from the token table because the user has logged out.*

- *Test Cases-*
	- *Also, we have done validation of the user input in the sign-up, login function. So, if a user doesn't enters the value as per the requirements, then corresponding error would be thrown.*
	- *Regex has been used for such validation, it could be seen in the views.py of the myauth application.*
	- *Here, we have also made sure that Email ID Field is not mandatory.*
	- *Here, also during Sign-up it checks whether any number is already registered before or not, if not then only it is allowed to sign-up*

- *Screenshots-*
	- ![login](snap/login.png)
	- ![logout](snap/logout.png)
	- ![signup](snap/signup.png)
	- ![get-token-1](snap/get-token-1.png)
	

#### AUTHOR-
- **coded by AAYUSH GADIA** 
- **contact info: gadia.aayush@gmail.com**
