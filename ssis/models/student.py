from . import cursor, db

class Student():
    def __init__(
        self, 
        id: str = None,
        firstName: str = None,
        middleName: str = None,
        lastName: str = None,
        yearLevel: str = None,
        gender: str = None,
        course: str = None,
        college: str = None,
        photo: str = None) -> None:
        
        self.id = id
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.yearLevel = yearLevel
        self.course = course
        self.college = college
        self.gender = gender
        self.photo = photo


    def get_all(self, page_num: int = None, item_per_page: int = None, paginate: bool = True) -> list:
        if not paginate:
            return self.student_list()
        offset = (page_num - 1) * item_per_page
        query = f'''
            SELECT id, 
                   firstname, 
                   middlename, 
                   lastname, 
                   gender, 
                   year, 
                   coursecode, 
                   photo, 
                   course.name, 
                   collegecode, 
                   college.name
            FROM students
            JOIN course
            ON students.coursecode = course.code
            JOIN college
            ON students.collegecode = college.code
            LIMIT {item_per_page} OFFSET {offset}
        '''
        cursor.execute(query)
        result = cursor.fetchall()
        students = [list(student) for student in result]
        return students
    
    
    @staticmethod
    def get_total() -> int:
        query = '''SELECT * FROM students'''
        cursor.execute(query)
        result = cursor.fetchall()
        total = len(result)
        return total
    
    
    @staticmethod
    def student_list() -> list:
        query = f'''
            SELECT id, 
                   firstname, 
                   middlename, 
                   lastname, 
                   gender, 
                   year, 
                   coursecode, 
                   photo, 
                   course.name, 
                   collegecode, 
                   college.name
            FROM students
            JOIN course
            ON students.coursecode = course.code
            JOIN college
            ON students.collegecode = college.code
        '''
        cursor.execute(query)
        result = cursor.fetchall()
        students = [list(student) for student in result]
        return students


    def search(self, keyword: str = None, field: str = None) -> list:
        keyword = keyword.upper()
        students = self.get_all(paginate=False)
        result = []

        if field is None: 
            result = self.search_by_field(students, keyword, 'all')
        elif field == 'id':
            result = self.search_by_field(students, keyword, 'id')
        elif field == 'firstname':
            result = self.search_by_field(students, keyword, 'firstname')
        elif field == 'middlename':
            result = self.search_by_field(students, keyword, 'middlename')
        elif field == 'lastname':
            result = self.search_by_field(students, keyword, 'lastname')
        elif field == 'gender':
            result = self.search_by_field(students, keyword, 'gender')
        elif field == 'year':
            result = self.search_by_field(students, keyword, 'year')
        elif field == 'course':
            result = self.search_by_field(students, keyword, 'course')
        
        return result


    @staticmethod
    def search_by_field(rows: list = None, keyword: str = None, field: str = None) -> list:
        result = []
        for row in rows:
            row_allcaps = [str(cell).upper() for cell in row]

            if field == 'all':
                if keyword in row_allcaps:
                    result.append(row)
            elif field == 'id':
                if keyword == row_allcaps[0]:
                    result.append(row)
                    return result
            elif field == 'firstname':
                if keyword == row_allcaps[1]:
                    result.append(row)
            elif field == 'middlename':
                if keyword == row_allcaps[2]:
                    result.append(row)
            elif field == 'lastname':
                if keyword == row_allcaps[3]:
                    result.append(row)
            elif field == 'gender':
                if keyword == row_allcaps[4]:
                    result.append(row)
            elif field == 'year':
                if keyword == row_allcaps[5]:
                    result.append(row)
            elif field == 'course':
                print('course', keyword, row_allcaps[6])
                if keyword == row_allcaps[6]:
                    result.append(row)

        return result


    @staticmethod
    def get_IDs() -> list:
        query = '''
            SELECT id
            FROM students
        '''
        cursor.execute(query)
        result = cursor.fetchall()
        IDs = [id[0] for id in result]
        return IDs
    

    @staticmethod
    def get_student(id: str = None) -> str:
        query = f'''
            SELECT id, 
                   firstname, 
                   middlename, 
                   lastname, 
                   gender, 
                   year, 
                   coursecode, 
                   collegecode
            FROM students
            WHERE id = '{id}'
        '''
        cursor.execute(query)
        student = list(cursor.fetchone())
        return student


    @staticmethod
    def get_image_url(id: str = None) -> str:
        query = f'''
            SELECT photo
            FROM students
            WHERE id = '{id}'
        '''
        cursor.execute(query)
        image_url = list(cursor.fetchone())
        return image_url
        

    def add_new(self) -> None:
        query = f'''
            INSERT INTO students (
                id, 
                firstname, 
                middlename, 
                lastname, 
                year, 
                gender, 
                coursecode, 
                collegecode,
                photo)
            VALUES (
                '{self.id}',
                '{self.firstName}',
                '{self.middleName}',
                '{self.lastName}',
                {self.yearLevel},
                '{self.gender}',
                '{self.course}',
                '{self.college}',
                '{self.photo}')
        '''
        cursor.execute(query)
        db.commit()
        return None
    

    @staticmethod
    def delete(id: str = None) -> None:
        query = f'''
            DELETE FROM students
            WHERE id='{id}'
        '''
        cursor.execute(query)
        db.commit()
        return None


    def update(self) -> None:
        if self.photo:
            query = f'''
                UPDATE students
                SET 
                    firstname = '{self.firstName}',
                    middlename = '{self.middleName}',
                    lastname = '{self.lastName}',
                    year = {self.yearLevel},
                    photo = '{self.photo}',
                    gender = '{self.gender}',
                    coursecode = '{self.course}',
                    collegecode = '{self.college}'
                WHERE
                    id = '{self.id}'
            '''
        else:
            query = f'''
                UPDATE students
                SET 
                    firstname = '{self.firstName}',
                    middlename = '{self.middleName}',
                    lastname = '{self.lastName}',
                    year = {self.yearLevel},
                    gender = '{self.gender}',
                    coursecode = '{self.course}',
                    collegecode = '{self.college}'
                WHERE
                    id = '{self.id}'
            '''
        cursor.execute(query)
        db.commit()
        return None


