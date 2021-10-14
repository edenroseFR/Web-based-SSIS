from ssis.models.college import College

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