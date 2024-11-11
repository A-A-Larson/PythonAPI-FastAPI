from databases import Database
from fastapi import FastAPI, HTTPException, status, Request
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from modules.student_module import (Student,
                                    errorNoValue,
                                    errorNotANumber,
                                    errorUnauthorizedRequest,
                                    errorIDDoesNotExist,
                                    StatusMessage,
                                    errorDBEmpty, StudentRequest, errorAgeEmpty,
                                    errorFirstNameEmpty, errorLastNameEmpty, errorGenderEmpty, errorEmailEmpty,
                                    errorPhoneEmpty, errorAddressEmpty, errorRegisteredEmpty, errorIDAlreadyExists)
from services.main_service import (get_all_tokens,
                                   convert_reply_to_token_list,
                                   get_student_by_id_query,
                                   get_all_students_query,
                                   convert_data_to_module, modify_student, add_student,
                                   get_all_classes_query, get_classes_by_student_id, convert_class_data_to_module,
                                   query_class_objects_list_to_enrollments_table)


app = FastAPI(title='Module 9-10',
              version='0.0.6',
              contact={'name': 'Andrew Larson', 'email': 'aalarson@mail.mccneb.edu'},
              description='INFO 1511 Final Project')

origins = ["*"]

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],)

database = Database('sqlite:///services/main.db')


tokens = []

@app.on_event('startup')
async def database_connect():                          #
    await database.connect()                           #
    reply = await database.fetch_all(get_all_tokens()) # Connection for use with tokens
    global tokens                                      #
    tokens = convert_reply_to_token_list(reply)        #


# @app.on_event('startup')      #
# async def database_connect(): # Connection for use with Swagger
#     await database.connect()  #


@app.on_event('shutdown')
async def database_disconnect():
    await database.disconnect()


@app.get("/student", response_model=Student, responses={200: {"model": Student}, 409: {"model": StatusMessage}, 400: {"model": StatusMessage}})
async def get_student(request: Request, student_id='NO VALUE'):

    if request.headers['Authorization'] not in tokens:
        raise HTTPException(status_code=status.HTTP_402_PAYMENT_REQUIRED, detail=errorUnauthorizedRequest)

    if student_id == 'NO VALUE':
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=errorNoValue)

    try:
        int(student_id)
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=errorNotANumber)

    try:
        student_list = await database.fetch_all(get_student_by_id_query(student_id))
        results = convert_data_to_module(student_list)
        return results[0]
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=errorIDDoesNotExist)


@app.get("/students", response_model=List[Student], responses={200: {"model": List[Student]}, 409: {"model": StatusMessage}, 400: {"model": StatusMessage}})
async def get_students(request: Request):

    if request.headers['Authorization'] not in tokens:
        raise HTTPException(status_code=status.HTTP_402_PAYMENT_REQUIRED, detail=errorUnauthorizedRequest)

    student_list = await database.fetch_all(get_all_students_query())
    results = convert_data_to_module(student_list)

    if not results:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=errorDBEmpty)

    return results


@app.post("/students/mod", response_model=str, responses={200: {"model": str}, 409: {"model": StatusMessage}, 400: {"model": StatusMessage}})
async def update_student(request: Request, student: StudentRequest):

    if request.headers['Authorization'] not in tokens:
        raise HTTPException(status_code=status.HTTP_402_PAYMENT_REQUIRED, detail=errorUnauthorizedRequest)

    if student.age == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=errorAgeEmpty)

    if student.firstName == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=errorFirstNameEmpty)

    if student.lastName == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=errorLastNameEmpty)

    if student.gender == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=errorGenderEmpty)

    if student.email == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=errorEmailEmpty)

    if student.phone == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=errorPhoneEmpty)

    if student.address == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=errorAddressEmpty)

    if student.registered == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=errorRegisteredEmpty)

    result = await database.fetch_all(get_student_by_id_query(student.student_id))

    if not result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=errorIDDoesNotExist)
    else:
        await database.execute(modify_student(student))
        query_class_objects_list_to_enrollments_table(student)
        return "Modified Student"


@app.post("/students/create", response_model=str, responses={200: {"model": str}, 409: {"model": StatusMessage}, 400: {"model": StatusMessage}})
async def create_student(request: Request, student: StudentRequest):

    if request.headers['Authorization'] not in tokens:
        raise HTTPException(status_code=status.HTTP_402_PAYMENT_REQUIRED, detail=errorUnauthorizedRequest)

    if student.age == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=errorAgeEmpty)

    if student.firstName == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=errorFirstNameEmpty)

    if student.lastName == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=errorLastNameEmpty)

    if student.gender == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=errorGenderEmpty)

    if student.email == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=errorEmailEmpty)

    if student.phone == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=errorPhoneEmpty)

    if student.address == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=errorAddressEmpty)

    if student.registered == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=errorRegisteredEmpty)

    result = await database.fetch_all(get_student_by_id_query(student.student_id))

    if result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=errorIDAlreadyExists)
    else:
        await database.execute(add_student(student))
        query_class_objects_list_to_enrollments_table(student)
        return "Added Student"

