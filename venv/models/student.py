from mysql_connection import cursor, db

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


    def showAll(self):
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


    def search(self, keyword=None):
        keyword = keyword.upper()
        students = self.showAll()
        result = []

        for student in students:
            student_allcaps = [str(info).upper() for info in student]
            if keyword in student_allcaps:
                result.append(student)
        return result

    @staticmethod
    def IDlist():
        query = '''
            SELECT id
            FROM students
        '''
        cursor.execute(query)
        result = cursor.fetchall()
        IDs = [id[0] for id in result]
        return IDs
    
    @staticmethod
    def get(id=None):
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

    def addNew(self):
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
    

    @staticmethod
    def delete(id=None):
        query = f'''
            DELETE FROM students
            WHERE id='{id}'
        '''
        cursor.execute(query)
        db.commit()


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
                collegecode = '{self.college}',
                photo = '{self.photo}'
            WHERE
                id = '{self.id}'
        '''
        cursor.execute(query)
        db.commit()


