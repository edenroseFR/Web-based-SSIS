from ssis.models.college import College

def add_college_to_db(college: str = None) -> bool:
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
            return None
        else:
            return False
    return False


def update_college_record(college: str = None) -> bool:
    code = college['code']
    name = college['name'].strip()
    
    if name:
        College(
            code,
            name
        ).update()
        return None
    else:
        return False