# PythonAPI-FastAPI
## Final project for a Python class. An API built using FastAPI framework

![image](https://github.com/user-attachments/assets/1200aa98-930f-4c09-bbee-6800e14aedba)
![image](https://github.com/user-attachments/assets/5ccc7eca-cc28-4262-9dcc-0afd73bc6707)

## How to install
Type "uvicorn main_controller:app" in main directory.
Use HTML files in main directory to test functionality. 
Edit HTML files as needed to test different POST calls.

## To make functional in Swagger:
### 1.
*Remove "request: Request" from endpoint functions and comment out:
"if request.headers['Authorization'] not in tokens:
        raise HTTPException(status_code=status.HTTP_402_PAYMENT_REQUIRED, detail=errorUnauthorizedRequest)"
from each endpoint.

### 2. Comment out:
tokens = []

 @app.on_event('startup')
 async def database_connect():                          
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;await database.connect()                           
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reply = await database.fetch_all(get_all_tokens())  Connection for use with tokens
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;global tokens                                      
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tokens = convert_reply_to_token_list(reply)        

### 3. Uncomment: 
@app.on_event('startup')      
async def database_connect():  Connection for use with Swagger
      await database.connect()  
