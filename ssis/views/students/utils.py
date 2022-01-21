from ssis.models.student import Student
from ssis.models.course import Course
from werkzeug.utils import secure_filename
import cloudinary.uploader as cloud
import os
from os import getenv

def add_student_to_db(student: list) -> bool:
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
                return True
            else:
                return False
        else:
            return False


def update_student_record(student: list = None) -> bool:
    id = student['id'].strip()
    firstname = student['firstname'].strip()
    middlename = student['middlename'].strip()
    lastname = student['lastname'].strip()
    gender = student['gender'].strip()
    yearlevel = student['yearlevel']
    course = student['course']
    photo = student['photo']
    
    if firstname and lastname:
        if photo:
            Student(
                id=id, 
                firstName=firstname,
                middleName=middlename, 
                lastName=lastname,
                photo=photo,
                yearLevel=yearlevel,
                gender=gender, 
                course=Course().get_coursecode_for(course),
                college=Course().get_collegecode(course)
            ).update()
        else:
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
        return None
    else:
        return False


def save_image(file: str = None) -> str:
    # parent_folder = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + \
    #                     '/static/entity_photos/students'
    # image = file
    # filename = secure_filename(file.filename)
    # image.save(os.path.join(parent_folder, filename))
    # return filename
    
    local_upload = 'local' == getenv('PHOTO_UPLOAD')
    if local_upload:
        parent_folder = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + \
                        '/static/entity_photos/students'
        image = file
        filename = secure_filename(file.filename)
        image.save(os.path.join(parent_folder, filename))
        return filename
    else:
        result = cloud.upload(file)
        url = result.get('url')
        return url


def delete_image(id: str = None) -> bool:
    local_upload = 'local' == getenv('LOCAL_UPLOAD')
    if not local_upload:
        image_url = (Student().get_image_url(id))[0]
        file_name = (image_url.split('/')[-1]).split('.')[0]
        print(file_name)
        cloud.destroy(file_name)
    return 


def check_page_limit(min: bool = None, max: bool = None) -> str:
    if min:
        return 'min'
    elif max:
        return 'max'
    else:
        return


def check_limit_validity(number_input: int = None, max_limit: int = None) -> int:
    if number_input < 5:
        return 5
    elif number_input > max_limit:
        return max_limit
    else:
        
        return number_input