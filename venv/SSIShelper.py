from models.student import Student
from models.course import Course
from models.college import College
from models.admin import Admin
import re

def userFound(username, password):
    if Admin(username,password).registeredUser():
        return True

def verified(username=None, password=None, password2=None):
    if username not in Admin().existingUsernames() and password == password2:
        Admin(username,password).register()
        return True

def allStudent():
    return Student().showAll()

def allCourse():
    return Course().showAll()

def allCollege():
    return College().showAll()

def searchStudent(search=None):
    return Student().search(keyword=search)

def addStudent(student):
    id = student['id'].strip()
    firstname = (student['firstname'].strip()).title()
    middlename = (student['middlename'].strip()).title()
    lastname = (student['lastname'].strip()).title()
    gender = student['gender'].strip()
    yearlevel = student['yearlevel']
    course = student['course']
    # ID validation
    if id:
        id_pattern = '^[0-9]{4}-[0-9]{4}$'
        if re.search(id_pattern, id) and id not in Student().IDlist():
            # Name validation
            if firstname and lastname:
                Student(
                    id=id, 
                    firstName=firstname, 
                    middleName=middlename, 
                    lastName=lastname,
                    yearLevel=yearlevel,
                    gender=gender,  
                    course=Course().courseCode(course), 
                    college=Course().collegeCode(course)
                ).addNew()
                return
            else:
                return False
        else:
            return False



def getStudent(id=None):
    return Student().get(id)


def updateStudent(student=None):
    id = student['id'].strip()
    firstname = student['firstname'].strip()
    middlename = student['middlename'].strip()
    lastname = student['lastname'].strip()
    gender = student['gender'].strip()
    yearlevel = student['yearlevel']
    course = student['course']
    
    if firstname and lastname:
        Student(
            id=id, 
            firstName=firstname,
            middleName=middlename, 
            lastName=lastname,
            yearLevel=yearlevel,
            gender=gender, 
            course=Course().courseCode(course), 
            college=Course().collegeCode(course)
        ).update()
        return
    else:
        return False


def deleteStudent(id=None):
    Student().delete(id)
    return


#Courses
def addCourse(course=None):
    code = (course['code'].strip()).upper()
    name = (course['name'].strip()).title()
    college = College().collegeCode(course['college'])
    # code validation
    if code and code not in Course().codeList():
        # name validation
        if name:
            Course(
                code,
                name,
                college
            ).addNew()
            return
        else:
            return False
    return False


def searchCourse(search=None):
    return Course().search(keyword=search)


def deleteCourse(id=None):
    Course().delete(id)
    return


def updateCourse(course=None):
    code = course['code']
    name = course['name'].strip()
    college = course['college']
    print(code,name,College().collegeCode(college))
    
    if code and name:
        Course(
            code,
            name,
            College().collegeCode(college)
        ).update()
        return
    else:
        return False


def searchCollege(search=None):
    return College().search(keyword=search)


def deleteCollege(id=None):
    College().delete(id)
    return


def addCollege(college=None):
    code = (college['code'].strip()).upper()
    name = (college['name'].strip()).title()
    # code validation
    if code and code not in College().codeList():
        # name validation
        if name:
            College(
                code,
                name
            ).addNew()
            return
        else:
            return False
    return False

def updateCollege(college=None):
    code = college['code']
    name = college['name'].strip()
    
    if name:
        College(
            code,
            name
        ).update()
        return
    else:
        return False

def collegeStatistics():
    return College().statistics()
