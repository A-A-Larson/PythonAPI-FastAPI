from modules.student_module import Student, StudentRequest, Class
import sqlite3 as sql


def get_student_by_id_query(student_id):
    return f'SELECT * FROM STUDENTS WHERE student_id={student_id}'


def get_all_students_query():
    return f'SELECT * from Students'


def modify_student(student: StudentRequest) -> str:
    return f'UPDATE Students SET currentlyEnrolled="{student.currentlyEnrolled}", age="{student.age}", firstName="{student.firstName}", lastName="{student.lastName}", gender="{student.gender}", email="{student.email}", phone="{student.phone}", address="{student.address}", registered="{student.registered}" WHERE student_id={student.student_id}'


def add_student(student: StudentRequest) -> str:
    return f'INSERT INTO Students (student_id, currentlyEnrolled, age, firstName, lastName, gender, email, phone, address, registered) VALUES ({student.student_id}, "{student.currentlyEnrolled}", "{student.age}", "{student.firstName}", "{student.lastName}", "{student.gender}", "{student.email}", "{student.phone}", "{student.address}", "{student.registered}")'


def query_class_objects_list_to_enrollments_table(student: StudentRequest):

    conn = sql.connect('./services/main.db')
    cur = conn.cursor()
    id_list = convert_class_objects_list_to_id_list(student)
    cur.execute(f'DELETE FROM Enrollment WHERE Enrollment.enrollment_student_id = {student.student_id}')
    for i in id_list:
        cur.execute(f'INSERT INTO Enrollment (enrollment_student_id, enrollment_class_id) VALUES ({student.student_id}, {i})')

    conn.commit()
    conn.close()


def convert_class_objects_list_to_id_list(student: StudentRequest):
    id_list = []
    for class_object in student.classes:
        id_list.append(class_object.class_id)
    return id_list


def get_all_classes_query():
    return f'SELECT * from Classes'


def get_classes_by_student_id(student_id):
    return f'SELECT class_id, code, title, description FROM Classes, Enrollment WHERE Classes.class_id = Enrollment.enrollment_class_id AND Enrollment.enrollment_student_id = {student_id}'


def get_all_tokens() -> str:
    return 'SELECT * FROM TOKENS'


def convert_reply_to_token_list(tuples):
    converted = []

    for token in tuples:
        converted.append(token[0])
    return converted


def convert_data_to_module(db_student_list):
    converted = []
    conn = sql.connect('./services/main.db')
    cur = conn.cursor()

    for student in db_student_list:
        db_class_list = cur.execute(get_classes_by_student_id(student.student_id))
        class_objects_list = convert_class_data_to_module(db_class_list)
        converted.append(Student(student_id=student[0],
                                 currentlyEnrolled=student[1],
                                 age=student[2],
                                 firstName=student[3],
                                 lastName=student[4],
                                 gender=student[5],
                                 email=student[6],
                                 phone=student[7],
                                 address=student[8],
                                 registered=student[9],
                                 classes=class_objects_list))

    conn.commit()
    conn.close()

    return converted


def convert_class_data_to_module(db_class_list):
    class_objects_list = []
    for i in db_class_list:
        class_objects_list.append(Class(class_id=i[0], code=i[1], title=i[2], description=i[3]))
    return class_objects_list

