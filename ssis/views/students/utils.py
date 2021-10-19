from ssis.models.student import Student
from ssis.models.course import Course
from werkzeug.utils import secure_filename
import os

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
                return None
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
        return None
    else:
        return False


def save_image(file: str = None, config=None) -> str:
    parent_folder = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + \
                    '\static\entity_photos\students'
    image = file
    filename = secure_filename(file.filename)
    image.save(os.path.join(parent_folder, filename))
    return filename
    
