from pydantic import BaseModel
from typing import List


class Class(BaseModel):
    class_id: int
    code: str
    title: str
    description: str


class Student(BaseModel):
    student_id: int
    currentlyEnrolled: bool
    firstName: str
    lastName: str
    age: str
    gender: str
    email: str
    phone: str
    address: str
    registered: str
    classes: List[Class]


class StudentRequest(BaseModel):
    student_id: int
    currentlyEnrolled: bool
    firstName: str
    lastName: str
    age: str
    gender: str
    email: str
    phone: str
    address: str
    registered: str
    classes: List[Class]


class StatusMessage(BaseModel):
    content: str


errorNoValue: StatusMessage = {'content': "You didn't provide a Student ID"}
errorNotANumber: StatusMessage = {'content': "Bad Request, Student ID must be a number"}
errorIDDoesNotExist: StatusMessage = {'content': "Bad Request, Student ID does not exist"}
errorIDAlreadyExists: StatusMessage = {'content': "Bad Request, Student ID already exists"}
errorDBEmpty: StatusMessage = {'content': "Bad Request, there are no students in the database"}
errorAgeEmpty: StatusMessage = {'content': "Bad Request, the age field was empty"}
errorFirstNameEmpty: StatusMessage = {'content': "Bad Request, the firstName field was empty"}
errorLastNameEmpty: StatusMessage = {'content': "Bad Request, the lastName field was empty"}
errorGenderEmpty: StatusMessage = {'content': "Bad Request, the gender field was empty"}
errorEmailEmpty: StatusMessage = {'content': "Bad Request, the email field was empty"}
errorPhoneEmpty: StatusMessage = {'content': "Bad Request, the phone field was empty"}
errorAddressEmpty: StatusMessage = {'content': "Bad Request, the address field was empty"}
errorRegisteredEmpty: StatusMessage = {'content': "Bad Request, the registered field was empty"}
errorUnauthorizedRequest: StatusMessage = {'content': "Unauthorized Request, token is not valid"}