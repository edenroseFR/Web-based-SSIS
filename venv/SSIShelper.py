from models.student import Student
from models.course import Course
from models.college import College
from models.admin import Admin
from werkzeug.utils import secure_filename
import os


def admin_found(username, password):
    if Admin(username,password).registered_user():
        return True


def verified(username=None, password=None, password2=None):
    if username not in Admin().get_usernames() and password == password2:
        Admin(username,password).register()
        return True



def add_student_to_db(student):
    id = student['id'].strip()
    firstname = (student['firstname'].strip()).title()
    middlename = (student['middlename'].strip()).title()
    lastname = (student['lastname'].strip()).title()
    gender = student['gender'].strip()
    yearlevel = student['yearlevel']
    course = student['course']
    photo = student['photo']
    # ID validation
    if id:
        if id not in Student().get_IDs():
            # Name validation
            if firstname and lastname:
                Student(
                    id=id, 
                    firstName=firstname, 
                    middleName=middlename, 
                    lastName=lastname,
                    yearLevel=yearlevel,
                    gender=gender,  
                    course=Course().get_coursecode_for(course),
                    college=Course().get_collegecode(course),
                    photo = photo
                ).add_new()
                return
            else:
                return False
        else:
            return False




def update_student_record(student=None):
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
            course=Course().get_coursecode_for(course),
            college=Course().get_collegecode(course)
        ).update()
        return
    else:
        return False




#Courses
def add_course_to_db(course=None):
    code = (course['code'].strip()).upper()
    name = (course['name'].strip()).title()
    college = College().get_collegecode_for(course['college'])
    # code validation
    if code and code not in Course().get_coursecodes():
        # name validation
        if name:
            Course(
                code,
                name,
                college
            ).add_new()
            return
        else:
            return False
    return False





def update_course_record(course=None):
    code = course['code']
    name = course['name'].strip()
    college = course['college']
    print(code, name, College().get_collegecode_for(college))
    
    if code and name:
        Course(
            code,
            name,
            College().get_collegecode_for(college)
        ).update()
        return
    else:
        return False



# Colleges
def add_college_to_db(college=None):
    code = (college['code'].strip()).upper()
    name = (college['name'].strip()).title()
    # code validation
    if code and code not in College().get_collegecodes():
        # name validation
        if name:
            College(
                code,
                name
            ).add_new()
            return
        else:
            return False
    return False


def update_college_record(college=None):
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





def save_image(file=None, config=None):
    image = file
    filename = secure_filename(file.filename)
    image.save(os.path.join(config, filename))
    return filename


def search_by_field(rows=None, keyword=None, field='id'):
    result = []
    for row in rows:
        row_allcaps = [str(cell).upper() for cell in row if cell != '']

        if field == 'all':
            if keyword in row_allcaps:
                result.append(row)
        if field == 'id':
            if keyword in row_allcaps[0]:
                result.append(row)
        elif field == 'firstname':
            if keyword in row_allcaps[1]:
                result.append(row)
        elif field == 'middlename':
            if keyword in row_allcaps[2]:
                result.append(row)
        elif field == 'lastname':
            if keyword in row_allcaps[3]:
                result.append(row)
        elif field == 'gender':
            if keyword in row_allcaps[4]:
                result.append(row)
        elif field == 'yearlevel':
            if keyword in row_allcaps[5]:
                result.append(row)
        elif field == 'course':
            if keyword in row_allcaps[8]:
                result.append(row)

    return result