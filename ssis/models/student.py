from . import cursor, db

class Student():
    def __init__(
        self, 
        id=None,
        firstName=None,
        middleName=None,
        lastName=None,
        yearLevel=None,
        gender=None,
        course=None,
        college=None,
        photo=None):
        
        self.id = id
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.yearLevel = yearLevel
        self.course = course
        self.college = college
        self.gender = gender
        self.photo = photo


    def get_all(self):
        query = '''
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


    def search(self, keyword=None, field=None):
        keyword = keyword.upper()
        students = self.get_all()
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
    def search_by_field(rows=None, keyword=None, field='id'):
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
    def get_IDs():
        query = '''
            SELECT id
            FROM students
        '''
        cursor.execute(query)
        result = cursor.fetchall()
        IDs = [id[0] for id in result]
        return IDs
    

    @staticmethod
    def get_student(id=None):
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

    def add_new(self):
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
                photo
            )
            VALUES (
                '{self.id}',
                '{self.firstName}',
                '{self.middleName}',
                '{self.lastName}',
                {self.yearLevel},
                '{self.gender}',
                '{self.course}',
                '{self.college}',
                '{self.photo}'
            )
        '''
        cursor.execute(query)
        db.commit()
        return None
    

    @staticmethod
    def delete(id=None):
        query = f'''
            DELETE FROM students
            WHERE id='{id}'
        '''
        cursor.execute(query)
        db.commit()
        return None


    def update(self):
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


