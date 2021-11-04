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