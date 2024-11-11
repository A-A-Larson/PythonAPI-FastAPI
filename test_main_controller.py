from os.path import dirname, abspath
from fastapi.testclient import TestClient
from main_controller import app
import sqlite3 as sql
import os


test_client = TestClient(app)


def test_get_student_no_id():
    response = test_client.get('/student')
    assert response.status_code == 409


def test_get_student_bad_id():
    response = test_client.get('/student?student_id=aa')
    assert response.status_code == 400


def test_get_student_id_does_not_exist():
    response = test_client.get('/student?student_id=99')
    assert response.status_code == 400


def test_get_student_id():
    response = test_client.get('/student?student_id=1')
    value = response.json()
    assert response.status_code == 200
    assert value['student_id'] == 1
    assert value['currentlyEnrolled'] == True
    assert value['firstName'] == 'Bray'
    assert value['lastName'] == 'Summers'
    assert value['age'] == '25'
    assert value['gender'] == 'male'
    assert value['email'] == 'braysummers@furnigeer.com'
    assert value['phone'] == '+1 (833) 417-2236'
    assert value['address'] == '184 Dekoven Court, Driftwood, Marshall Islands, 6520'
    assert value['registered'] == 'Mon Aug 06 2018 04:13:31'


def test_get_students_status_200():
    response = test_client.get('/students')
    assert response.status_code == 200


def test_get_students():
    response = test_client.get('/students')
    assert len(response.read()) > 0


def test_update_student():
    response = test_client.post('/students/mod',
                                json={'student_id': 0,
                                      'currentlyEnrolled': True,
                                      'age': '22',
                                      'firstName': 'Jane',
                                      'lastName': 'Doe',
                                      'gender': 'male',
                                      'email': 'janedoe@furnigeer.com',
                                      'phone': '+1 (849) 512-2232',
                                      'address': '123 Easy Street, Tyro, Nebraska, 6696',
                                      'registered': 'Thurs Feb 19 2020 07:25:47',
                                      'classes':
                                          [
                                              {
                                                  "class_id": 0,
                                                  "code": "INFO 1003",
                                                  "title": "Basic Programming",
                                                  "description": "Basic programming class using Python."
                                              }
                                          ]
                                      })
    assert response.status_code == 200
    assert "Modified Student" in response.json()


def test_update_student_id_does_not_exist():
    response = test_client.post('/students/mod',
                                json={'student_id': 999,
                                      'currentlyEnrolled': True,
                                      'age': '22',
                                      'firstName': 'Jane',
                                      'lastName': 'Doe',
                                      'gender': 'male',
                                      'email': 'janedoe@furnigeer.com',
                                      'phone': '+1 (849) 512-2232',
                                      'address': '123 Easy Street, Tyro, Nebraska, 6696',
                                      'registered': 'Thurs Feb 19 2020 07:25:47',
                                      'classes':
                                          [
                                              {
                                                  "class_id": 0,
                                                  "code": "INFO 1003",
                                                  "title": "Basic Programming",
                                                  "description": "Basic programming class using Python."
                                              }
                                          ]
                                      })
    assert response.status_code == 400


def test_update_student_empty_age():
    response = test_client.post('/students/mod',
                                json={'student_id': 0,
                                      'currentlyEnrolled': True,
                                      'age': '',
                                      'firstName': 'Jane',
                                      'lastName': 'Doe',
                                      'gender': 'male',
                                      'email': 'janedoe@furnigeer.com',
                                      'phone': '+1 (849) 512-2232',
                                      'address': '123 Easy Street, Tyro, Nebraska, 6696',
                                      'registered': 'Thurs Feb 19 2020 07:25:47',
                                      'classes':
                                          [
                                              {
                                                  "class_id": 0,
                                                  "code": "INFO 1003",
                                                  "title": "Basic Programming",
                                                  "description": "Basic programming class using Python."
                                              }
                                          ]
                                      })
    assert response.status_code == 400


def test_update_student_empty_firstname():
    response = test_client.post('/students/mod',
                                json={'student_id': 0,
                                      'currentlyEnrolled': True,
                                      'age': '22',
                                      'firstName': '',
                                      'lastName': 'Doe',
                                      'gender': 'male',
                                      'email': 'janedoe@furnigeer.com',
                                      'phone': '+1 (849) 512-2232',
                                      'address': '123 Easy Street, Tyro, Nebraska, 6696',
                                      'registered': 'Thurs Feb 19 2020 07:25:47',
                                      'classes':
                                          [
                                              {
                                                  "class_id": 0,
                                                  "code": "INFO 1003",
                                                  "title": "Basic Programming",
                                                  "description": "Basic programming class using Python."
                                              }
                                          ]
                                      })
    assert response.status_code == 400


def test_update_student_empty_lastname():
    response = test_client.post('/students/mod',
                                json={'student_id': 0,
                                      'currentlyEnrolled': True,
                                      'age': '22',
                                      'firstName': 'Jane',
                                      'lastName': '',
                                      'gender': 'male',
                                      'email': 'janedoe@furnigeer.com',
                                      'phone': '+1 (849) 512-2232',
                                      'address': '123 Easy Street, Tyro, Nebraska, 6696',
                                      'registered': 'Thurs Feb 19 2020 07:25:47',
                                      'classes':
                                          [
                                              {
                                                  "class_id": 0,
                                                  "code": "INFO 1003",
                                                  "title": "Basic Programming",
                                                  "description": "Basic programming class using Python."
                                              }
                                          ]
                                      })
    assert response.status_code == 400


def test_update_student_empty_gender():
    response = test_client.post('/students/mod',
                                json={'student_id': 0,
                                      'currentlyEnrolled': True,
                                      'age': '22',
                                      'firstName': 'Jane',
                                      'lastName': 'Doe',
                                      'gender': '',
                                      'email': 'janedoe@furnigeer.com',
                                      'phone': '+1 (849) 512-2232',
                                      'address': '123 Easy Street, Tyro, Nebraska, 6696',
                                      'registered': 'Thurs Feb 19 2020 07:25:47',
                                      'classes':
                                          [
                                              {
                                                  "class_id": 0,
                                                  "code": "INFO 1003",
                                                  "title": "Basic Programming",
                                                  "description": "Basic programming class using Python."
                                              }
                                          ]
                                      })
    assert response.status_code == 400


def test_update_student_empty_email():
    response = test_client.post('/students/mod',
                                json={'student_id': 0,
                                      'currentlyEnrolled': True,
                                      'age': '22',
                                      'firstName': 'Jane',
                                      'lastName': 'Doe',
                                      'gender': 'male',
                                      'email': '',
                                      'phone': '+1 (849) 512-2232',
                                      'address': '123 Easy Street, Tyro, Nebraska, 6696',
                                      'registered': 'Thurs Feb 19 2020 07:25:47',
                                      'classes':
                                          [
                                              {
                                                  "class_id": 0,
                                                  "code": "INFO 1003",
                                                  "title": "Basic Programming",
                                                  "description": "Basic programming class using Python."
                                              }
                                          ]
                                      })
    assert response.status_code == 400


def test_update_student_empty_phone():
    response = test_client.post('/students/mod',
                                json={'student_id': 0,
                                      'currentlyEnrolled': True,
                                      'age': '22',
                                      'firstName': 'Jane',
                                      'lastName': 'Doe',
                                      'gender': 'male',
                                      'email': 'janedoe@furnigeer.com',
                                      'phone': '',
                                      'address': '123 Easy Street, Tyro, Nebraska, 6696',
                                      'registered': 'Thurs Feb 19 2020 07:25:47',
                                      'classes':
                                          [
                                              {
                                                  "class_id": 0,
                                                  "code": "INFO 1003",
                                                  "title": "Basic Programming",
                                                  "description": "Basic programming class using Python."
                                              }
                                          ]
                                      })
    assert response.status_code == 400


def test_update_student_empty_address():
    response = test_client.post('/students/mod',
                                json={'student_id': 0,
                                      'currentlyEnrolled': True,
                                      'age': '22',
                                      'firstName': 'Jane',
                                      'lastName': 'Doe',
                                      'gender': 'male',
                                      'email': 'janedoe@furnigeer.com',
                                      'phone': '+1 (849) 512-2232',
                                      'address': '',
                                      'registered': 'Thurs Feb 19 2020 07:25:47',
                                      'classes':
                                          [
                                              {
                                                  "class_id": 0,
                                                  "code": "INFO 1003",
                                                  "title": "Basic Programming",
                                                  "description": "Basic programming class using Python."
                                              }
                                          ]
                                      })
    assert response.status_code == 400


def test_update_student_empty_registered():
    response = test_client.post('/students/mod',
                                json={'student_id': 0,
                                      'currentlyEnrolled': True,
                                      'age': '22',
                                      'firstName': 'Jane',
                                      'lastName': 'Doe',
                                      'gender': 'male',
                                      'email': 'janedoe@furnigeer.com',
                                      'phone': '+1 (849) 512-2232',
                                      'address': '123 Easy Street, Tyro, Nebraska, 6696',
                                      'registered': '',
                                      'classes':
                                          [
                                              {
                                                  "class_id": 0,
                                                  "code": "INFO 1003",
                                                  "title": "Basic Programming",
                                                  "description": "Basic programming class using Python."
                                              }
                                          ]
                                      })
    assert response.status_code == 400


def test_create_student():
    response = test_client.post('/students/create',
                                json={'student_id': 90,
                                      'currentlyEnrolled': True,
                                      'age': '22',
                                      'firstName': 'Jane',
                                      'lastName': 'Doe',
                                      'gender': 'male',
                                      'email': 'janedoe@furnigeer.com',
                                      'phone': '+1 (849) 512-2232',
                                      'address': '123 Easy Street, Tyro, Nebraska, 6696',
                                      'registered': 'Thurs Feb 19 2020 07:25:47',
                                      'classes':
                                          [
                                              {
                                                  "class_id": 0,
                                                  "code": "INFO 1003",
                                                  "title": "Basic Programming",
                                                  "description": "Basic programming class using Python."
                                              }
                                          ]
                                      })
    assert response.status_code == 200
    assert "Added Student" in response.json()


def test_create_student_id_already_exists():
    response = test_client.post('/students/create',
                                json={'student_id': 90,
                                      'currentlyEnrolled': True,
                                      'age': '22',
                                      'firstName': 'Jane',
                                      'lastName': 'Doe',
                                      'gender': 'male',
                                      'email': 'janedoe@furnigeer.com',
                                      'phone': '+1 (849) 512-2232',
                                      'address': '123 Easy Street, Tyro, Nebraska, 6696',
                                      'registered': 'Thurs Feb 19 2020 07:25:47',
                                      'classes':
                                          [
                                              {
                                                  "class_id": 0,
                                                  "code": "INFO 1003",
                                                  "title": "Basic Programming",
                                                  "description": "Basic programming class using Python."
                                              }
                                          ]
                                      })
    assert response.status_code == 400


def test_create_student_empty_age():
    response = test_client.post('/students/create',
                                json={'student_id': 91,
                                      'currentlyEnrolled': True,
                                      'age': '',
                                      'firstName': 'Jane',
                                      'lastName': 'Doe',
                                      'gender': 'male',
                                      'email': 'janedoe@furnigeer.com',
                                      'phone': '+1 (849) 512-2232',
                                      'address': '123 Easy Street, Tyro, Nebraska, 6696',
                                      'registered': 'Thurs Feb 19 2020 07:25:47',
                                      'classes':
                                          [
                                              {
                                                  "class_id": 0,
                                                  "code": "INFO 1003",
                                                  "title": "Basic Programming",
                                                  "description": "Basic programming class using Python."
                                              }
                                          ]
                                      })
    assert response.status_code == 400


def test_create_student_empty_firstname():
    response = test_client.post('/students/create',
                                json={'student_id': 92,
                                      'currentlyEnrolled': True,
                                      'age': '22',
                                      'firstName': '',
                                      'lastName': 'Doe',
                                      'gender': 'male',
                                      'email': 'janedoe@furnigeer.com',
                                      'phone': '+1 (849) 512-2232',
                                      'address': '123 Easy Street, Tyro, Nebraska, 6696',
                                      'registered': 'Thurs Feb 19 2020 07:25:47',
                                      'classes':
                                          [
                                              {
                                                  "class_id": 0,
                                                  "code": "INFO 1003",
                                                  "title": "Basic Programming",
                                                  "description": "Basic programming class using Python."
                                              }
                                          ]
                                      })
    assert response.status_code == 400


def test_create_student_empty_lastname():
    response = test_client.post('/students/create',
                                json={'student_id': 93,
                                      'currentlyEnrolled': True,
                                      'age': '22',
                                      'firstName': 'Jane',
                                      'lastName': '',
                                      'gender': 'male',
                                      'email': 'janedoe@furnigeer.com',
                                      'phone': '+1 (849) 512-2232',
                                      'address': '123 Easy Street, Tyro, Nebraska, 6696',
                                      'registered': 'Thurs Feb 19 2020 07:25:47',
                                      'classes':
                                          [
                                              {
                                                  "class_id": 0,
                                                  "code": "INFO 1003",
                                                  "title": "Basic Programming",
                                                  "description": "Basic programming class using Python."
                                              }
                                          ]
                                      })
    assert response.status_code == 400


def test_create_student_empty_gender():
    response = test_client.post('/students/create',
                                json={'student_id': 94,
                                      'currentlyEnrolled': True,
                                      'age': '22',
                                      'firstName': 'Jane',
                                      'lastName': 'Doe',
                                      'gender': '',
                                      'email': 'janedoe@furnigeer.com',
                                      'phone': '+1 (849) 512-2232',
                                      'address': '123 Easy Street, Tyro, Nebraska, 6696',
                                      'registered': 'Thurs Feb 19 2020 07:25:47',
                                      'classes':
                                          [
                                              {
                                                  "class_id": 0,
                                                  "code": "INFO 1003",
                                                  "title": "Basic Programming",
                                                  "description": "Basic programming class using Python."
                                              }
                                          ]
                                      })
    assert response.status_code == 400


def test_create_student_empty_email():
    response = test_client.post('/students/create',
                                json={'student_id': 95,
                                      'currentlyEnrolled': True,
                                      'age': '22',
                                      'firstName': 'Jane',
                                      'lastName': 'Doe',
                                      'gender': 'male',
                                      'email': '',
                                      'phone': '+1 (849) 512-2232',
                                      'address': '123 Easy Street, Tyro, Nebraska, 6696',
                                      'registered': 'Thurs Feb 19 2020 07:25:47',
                                      'classes':
                                          [
                                              {
                                                  "class_id": 0,
                                                  "code": "INFO 1003",
                                                  "title": "Basic Programming",
                                                  "description": "Basic programming class using Python."
                                              }
                                          ]
                                      })
    assert response.status_code == 400


def test_create_student_empty_phone():
    response = test_client.post('/students/create',
                                json={'student_id': 96,
                                      'currentlyEnrolled': True,
                                      'age': '22',
                                      'firstName': 'Jane',
                                      'lastName': 'Doe',
                                      'gender': 'male',
                                      'email': 'janedoe@furnigeer.com',
                                      'phone': '',
                                      'address': '123 Easy Street, Tyro, Nebraska, 6696',
                                      'registered': 'Thurs Feb 19 2020 07:25:47',
                                      'classes':
                                          [
                                              {
                                                  "class_id": 0,
                                                  "code": "INFO 1003",
                                                  "title": "Basic Programming",
                                                  "description": "Basic programming class using Python."
                                              }
                                          ]
                                      })
    assert response.status_code == 400


def test_create_student_empty_address():
    response = test_client.post('/students/create',
                                json={'student_id': 97,
                                      'currentlyEnrolled': True,
                                      'age': '22',
                                      'firstName': 'Jane',
                                      'lastName': 'Doe',
                                      'gender': 'male',
                                      'email': 'janedoe@furnigeer.com',
                                      'phone': '+1 (849) 512-2232',
                                      'address': '',
                                      'registered': 'Thurs Feb 19 2020 07:25:47',
                                      'classes':
                                          [
                                              {
                                                  "class_id": 0,
                                                  "code": "INFO 1003",
                                                  "title": "Basic Programming",
                                                  "description": "Basic programming class using Python."
                                              }
                                          ]
                                      })
    assert response.status_code == 400


def test_create_student_empty_registered():
    response = test_client.post('/students/create',
                                json={'student_id': 98,
                                      'currentlyEnrolled': True,
                                      'age': '22',
                                      'firstName': 'Jane',
                                      'lastName': 'Doe',
                                      'gender': 'male',
                                      'email': 'janedoe@furnigeer.com',
                                      'phone': '+1 (849) 512-2232',
                                      'address': '123 Easy Street, Tyro, Nebraska, 6696',
                                      'registered': '',
                                      'classes':
                                          [
                                              {
                                                  "class_id": 0,
                                                  "code": "INFO 1003",
                                                  "title": "Basic Programming",
                                                  "description": "Basic programming class using Python."
                                              }
                                          ]
                                      })
    assert response.status_code == 400


def test_get_students_status_400():
    conn = sql.connect('./services/main.db')#
    cur = conn.cursor()                     #
    cur.execute('DELETE FROM Students')     # empty table to test for empty db
    conn.commit()                           #
    conn.close()                            #
    response = test_client.get('/students')
    assert response.status_code == 400
    os.remove("./services/main.db")                             # delete db file
    os.chdir(dirname(abspath("./services/database_creator.py")))# change cwd to db creator
    exec(open("database_creator.py").read())                    # reset db

