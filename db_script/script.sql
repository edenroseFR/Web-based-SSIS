DROP DATABASE IF EXISTS `ssisdb`;
CREATE DATABASE IF NOT EXISTS `ssisdb`;
USE `ssisdb`;

CREATE TABLE `admin`(
username VARCHAR(20) NOT NULL,
password VARCHAR(100) NOT NULL,
PRIMARY KEY(username)
);

INSERT INTO `admin`(`username`, `password`)
VALUES ('eden', 'sha256$ULUS96W3djTrRi7e$233ff68eb2b2c3593440e1d6c0dabaaea17a9f246328db4ab1f09d05f5929568');

CREATE TABLE `course`(
code VARCHAR(10) NOT NULL,
name VARCHAR(50) NOT NULL,
college VARCHAR(45) NOT NULL,
PRIMARY KEY(code)
);

CREATE TABLE `college`(
code VARCHAR(10) NOT NULL,
name VARCHAR(50) NOT NULL,
PRIMARY KEY(code)
);

CREATE TABLE `students`(
id VARCHAR(9) NOT NULL,
firstname VARCHAR(50) NOT NULL,
middlename VARCHAR(20) NOT NULL,
lastname VARCHAR(20) NOT NULL,
year INT(1) NOT NULL,
gender VARCHAR(10) NOT NULL,
coursecode VARCHAR(10) NOT NULL,
collegecode VARCHAR(10),
photo VARCHAR(500),
PRIMARY KEY(id),
FOREIGN KEY(coursecode) REFERENCES course(code),
FOREIGN KEY(collegecode) REFERENCES college(code)
);

INSERT INTO `college`(`code`, `name`)
VALUES ('CCS', 'College of Computer Studies'),
	   ('CSM', 'College of Science and Mathematics'),
       ('CASS', 'College of Arts and Social Sciences'),
       ('COET', 'College of Engineering and Technology'),
       ('CED', 'College of Education'),
       ('CON', 'College of Nursing');

INSERT INTO `course`(`code`, `name`, `college`)
VALUES ('BSCS', 'Bachelor of Science in Computer Science', 'CCS'),
	   ('BSIT', 'Bachelor of Science in Information Technology', 'CCS'),
       ('BSIS', 'Bachelor of Science in Information System', 'CCS'),
       ('BSCE', 'Bachelor of Science in Civil Engineering', 'COET'),
       ('BSChemEng', 'Bachelor of Science in Chemical Engineering', 'CCS');
