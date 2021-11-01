from ssis.models.course import Course
from ssis.models.college import College

def add_course_to_db(course: str = None) -> bool:
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
            return None
        else:
            return False
    return False



def update_course_record(course: str = None) -> bool:
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
        return None
    else:
        return False