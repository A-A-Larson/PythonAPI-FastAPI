import sqlite3 as sql

conn = sql.connect('main.db')
cur = conn.cursor()
createTable = 'CREATE TABLE Students (student_id INTEGER not null primary key, currentlyEnrolled VARCHAR(5), age VARCHAR(3), firstName VARCHAR(30), lastName VARCHAR(30), gender VARCHAR(6), email VARCHAR(30), phone VARCHAR(20), address VARCHAR(50), registered VARCHAR(30))'
cur.execute(createTable)

cur.execute('INSERT INTO Students VALUES (0, "False", "21", "Veronica", "Potter", "female", "veronicapotter@furnigeer.com", "+1 (849) 512-2231", "771 Downing Street, Tyro, Nebraska, 6696", "Wed Feb 19 2020 07:25:47")')
cur.execute('INSERT INTO Students VALUES (1, "True", "25", "Bray", "Summers", "male", "braysummers@furnigeer.com", "+1 (833) 417-2236", "184 Dekoven Court, Driftwood, Marshall Islands, 6520", "Mon Aug 06 2018 04:13:31")')
cur.execute('INSERT INTO Students VALUES (2, "False", "38", "Isabelle", "Robles", "female", "isabellerobles@furnigeer.com", "+1 (830) 458-3893", "250 Jamaica Avenue, Elrama, District Of Columbia, 1166", "Tue Nov 28 2017 19:13:59")')
cur.execute('INSERT INTO Students VALUES (3, "False", "25", "Cynthia", "Campbell", "female", "cynthiacampbell@furnigeer.com", "+1 (900) 441-2849", "816 Preston Court, Coinjock, Wisconsin, 9858", "Wed Sep 27 2017 12:42:10")')
cur.execute('INSERT INTO Students VALUES (4, "False", "21", "Holder", "Livingston", "male", "holderlivingston@furnigeer.com", "+1 (943) 407-3952", "380 Prospect Street, Adelino, New Hampshire, 4695", "Sat Sep 21 2019 19:58:47")')
cur.execute('INSERT INTO Students VALUES (5, "False", "29", "Bentley", "Burke", "male", "bentleyburke@furnigeer.com", "+1 (804) 565-2529", "950 Kingston Avenue, Ribera, American Samoa, 2016", "Tue Feb 09 2021 04:07:36")')
cur.execute('INSERT INTO Students VALUES (6, "True", "34", "Velazquez", "Lucas", "male", "velazquezlucas@furnigeer.com", "+1 (919) 519-3148", "148 Beacon Court, Bradenville, Connecticut, 4771", "Fri Aug 27 2021 04:49:06")')
cur.execute('INSERT INTO Students VALUES (7, "True", "26", "Blevins", "Farmer", "male", "blevinsfarmer@furnigeer.com", "+1 (962) 490-2957", "425 Ridge Court, Dotsero, South Carolina, 3021", "Mon Oct 12 2015 15:41:49")')
cur.execute('INSERT INTO Students VALUES (8, "True", "37", "Doyle", "Camacho", "male", "doylecamacho@furnigeer.com", "+1 (909) 436-2106", "812 Christopher Avenue, Kiskimere, Palau, 175", "Thu Jan 10 2019 16:19:30")')
cur.execute('INSERT INTO Students VALUES (9, "False", "18", "Donovan", "Rowe", "male", "donovanrowe@furnigeer.com", "+1 (812) 464-3111", "490 Alice Court, Bangor, Maine, 979", "Sat Nov 28 2020 13:59:50")')
cur.execute('INSERT INTO Students VALUES (10, "True", "25", "Estelle", "Casey", "female", "estellecasey@furnigeer.com", "+1 (846) 424-3549", "470 Senator Street, Lindcove, Northern Mariana Islands, 927", "Tue Dec 12 2017 01:00:47")')
cur.execute('INSERT INTO Students VALUES (11, "True", "26", "Sherman", "Gay", "male", "shermangay@furnigeer.com", "+1 (849) 447-2805", "145 Lamont Court, Spelter, New Mexico, 7050", "Wed Jan 20 2016 00:48:42")')
cur.execute('INSERT INTO Students VALUES (12, "False", "26", "Cummings", "Hester", "male", "cummingshester@furnigeer.com", "+1 (935) 590-2194", "323 Division Avenue, Hobucken, Federated States Of Micronesia, 6081", "Wed Mar 16 2022 09:44:27")')
cur.execute('INSERT INTO Students VALUES (13, "True", "28", "Allyson", "Wiggins", "female", "allysonwiggins@furnigeer.com", "+1 (934) 514-3729", "759 Bergen Street, Fairforest, Alabama, 7393", "Fri Apr 23 2021 09:42:15")')
cur.execute('INSERT INTO Students VALUES (14, "True", "20", "Powell", "Walsh", "male", "powellwalsh@furnigeer.com", "+1 (922) 572-3476", "138 Glendale Court, Gratton, California, 2403", "Thu Dec 10 2015 19:44:09")')

print(cur.execute('SELECT * from Students').fetchall())


createTable = ('CREATE TABLE Classes ('
               'class_id INTEGER not null primary key, '
               'code VARCHAR(9), '
               'title VARCHAR(60), '
               'description VARCHAR(60))')
cur.execute(createTable)

cur.execute('INSERT INTO Classes VALUES (0, "INFO 1003", "Basic Programming", "Basic programming class using Python.")')
cur.execute('INSERT INTO Classes VALUES (1, "INFO 1001", "Intro to Programming", "Visual programming class")')
cur.execute('INSERT INTO Classes VALUES (2, "INFO 1002", "Intro to Web Development", "Basics of HTML and CSS")')
cur.execute('INSERT INTO Classes VALUES (3, "INFO 1004", "Programming I", "Advanced topics of programming")')
cur.execute('INSERT INTO Classes VALUES (4, "INFO 1005", "Intro to Database", "Basics of database design and development class.")')
cur.execute('INSERT INTO Classes VALUES (5, "INFO 1011", "Intro to C#", "Programming class using C# language.")')
cur.execute('INSERT INTO Classes VALUES (6, "INFO 1010", "Intro to Java", "Programming class using Java language.")')
cur.execute('INSERT INTO Classes VALUES (7, "INFO 1021", "Advanced C#", "Advanced Programming Class using C# language")')
cur.execute('INSERT INTO Classes VALUES (8, "INFO 1020", "Advanced Java", "Advanced Programming Class using Java language")')
cur.execute('INSERT INTO Classes VALUES (9, "INFO 1015", "Intro to AWS", "Basics of Cloud services using AWS")')
cur.execute('INSERT INTO Classes VALUES (10, "INFO 1014", "Intro to Azure", "Basics of Cloud services using Azure")')
cur.execute('INSERT INTO Classes VALUES (11, "INFO 1012", "Intro to Game Development", "Basics of Game Development using Unity3d Engine")')
cur.execute('INSERT INTO Classes VALUES (12, "INFO 1022", "Advanced to Game Development", "Advanced Game Development using Unity3d Engine")')
cur.execute('INSERT INTO Classes VALUES (13, "INFO 1032", "Intro to .NET", "Basics of .NET Framework")')
cur.execute('INSERT INTO Classes VALUES (14, "INFO 1101", "Intro to Spring Boot", "Basics of Spring Boot using Java")')
cur.execute('INSERT INTO Classes VALUES (15, "INFO 1102", "Advanced Spring Boot", "Advanced topics of Spring Boot with Java.")')

print(cur.execute('SELECT * FROM Classes').fetchall())


createTable = ('CREATE TABLE Enrollment ('
                'enrollment_id INTEGER not null primary key, '
                'enrollment_student_id INTEGER, '
                'enrollment_class_id INTEGER,'
                'FOREIGN KEY(enrollment_student_id) REFERENCES Students(student_id)'
                'FOREIGN KEY(enrollment_class_id) REFERENCES Classes(class_id))')
cur.execute(createTable)

cur.execute('INSERT INTO Enrollment VALUES (0, 0, 0)')
cur.execute('INSERT INTO Enrollment VALUES (1, 0, 2)')
cur.execute('INSERT INTO Enrollment VALUES (2, 0, 14)')
cur.execute('INSERT INTO Enrollment VALUES (3, 0, 9)')
cur.execute('INSERT INTO Enrollment VALUES (4, 1, 1)')
cur.execute('INSERT INTO Enrollment VALUES (5, 1, 9)')
cur.execute('INSERT INTO Enrollment VALUES (6, 1, 4)')
cur.execute('INSERT INTO Enrollment VALUES (7, 1, 14)')
cur.execute('INSERT INTO Enrollment VALUES (8, 2, 11)')
cur.execute('INSERT INTO Enrollment VALUES (9, 2, 12)')
cur.execute('INSERT INTO Enrollment VALUES (10, 2, 13)')
cur.execute('INSERT INTO Enrollment VALUES (11, 3, 1)')
cur.execute('INSERT INTO Enrollment VALUES (12, 4, 5)')
cur.execute('INSERT INTO Enrollment VALUES (13, 4, 7)')
cur.execute('INSERT INTO Enrollment VALUES (14, 4, 14)')
cur.execute('INSERT INTO Enrollment VALUES (15, 4, 2)')
cur.execute('INSERT INTO Enrollment VALUES (16, 4, 1)')
cur.execute('INSERT INTO Enrollment VALUES (17, 5, 15)')
cur.execute('INSERT INTO Enrollment VALUES (18, 5, 12)')
cur.execute('INSERT INTO Enrollment VALUES (19, 5, 13)')
cur.execute('INSERT INTO Enrollment VALUES (20, 6, 6)')
cur.execute('INSERT INTO Enrollment VALUES (21, 6, 8)')
cur.execute('INSERT INTO Enrollment VALUES (22, 6, 13)')
cur.execute('INSERT INTO Enrollment VALUES (23, 7, 1)')
cur.execute('INSERT INTO Enrollment VALUES (24, 7, 2)')
cur.execute('INSERT INTO Enrollment VALUES (25, 7, 3)')
cur.execute('INSERT INTO Enrollment VALUES (26, 8, 2)')
cur.execute('INSERT INTO Enrollment VALUES (27, 8, 4)')
cur.execute('INSERT INTO Enrollment VALUES (28, 8, 7)')
cur.execute('INSERT INTO Enrollment VALUES (29, 8, 10)')
cur.execute('INSERT INTO Enrollment VALUES (30, 8, 15)')
cur.execute('INSERT INTO Enrollment VALUES (31, 9, 0)')
cur.execute('INSERT INTO Enrollment VALUES (32, 9, 1)')
cur.execute('INSERT INTO Enrollment VALUES (33, 9, 3)')
cur.execute('INSERT INTO Enrollment VALUES (34, 9, 5)')
cur.execute('INSERT INTO Enrollment VALUES (35, 9, 15)')
cur.execute('INSERT INTO Enrollment VALUES (36, 10, 10)')
cur.execute('INSERT INTO Enrollment VALUES (37, 10, 4)')
cur.execute('INSERT INTO Enrollment VALUES (38, 10, 13)')
cur.execute('INSERT INTO Enrollment VALUES (39, 11, 9)')
cur.execute('INSERT INTO Enrollment VALUES (40, 11, 4)')
cur.execute('INSERT INTO Enrollment VALUES (41, 11, 3)')
cur.execute('INSERT INTO Enrollment VALUES (42, 11, 5)')
cur.execute('INSERT INTO Enrollment VALUES (43, 11, 1)')
cur.execute('INSERT INTO Enrollment VALUES (44, 12, 3)')
cur.execute('INSERT INTO Enrollment VALUES (45, 12, 4)')
cur.execute('INSERT INTO Enrollment VALUES (46, 12, 9)')
cur.execute('INSERT INTO Enrollment VALUES (47, 12, 6)')
cur.execute('INSERT INTO Enrollment VALUES (48, 12, 14)')
cur.execute('INSERT INTO Enrollment VALUES (49, 13, 11)')
cur.execute('INSERT INTO Enrollment VALUES (50, 13, 12)')
cur.execute('INSERT INTO Enrollment VALUES (51, 13, 2)')
cur.execute('INSERT INTO Enrollment VALUES (52, 14, 0)')
cur.execute('INSERT INTO Enrollment VALUES (53, 14, 10)')
cur.execute('INSERT INTO Enrollment VALUES (54, 14, 5)')

print(cur.execute('SELECT * from Enrollment').fetchall())

createTable = 'CREATE TABLE TOKENS (TOKEN VARCHAR(30))'
cur.execute(createTable)

cur.execute('INSERT INTO TOKENS VALUES ("C2PxpPAUXW")')
cur.execute('INSERT INTO TOKENS VALUES ("l2sY67lg06")')
cur.execute('INSERT INTO TOKENS VALUES ("3CpKUPVoaw")')
cur.execute('INSERT INTO TOKENS VALUES ("E5CwltZJ7R")')
cur.execute('INSERT INTO TOKENS VALUES ("DnPipi1mU6")')

print(cur.execute('SELECT * from TOKENS').fetchall())

conn.commit()
conn.close()