from mysql_connection import cursor, db

class Course():
    def __init__(
        self, 
        code=None,
        name=None,
        college=None,):
        
        self.code = code
        self.name = name
        self.college = college
    

    def showAll(self):
        query = '''
            SELECT code, name, college
            FROM course;
        '''
        cursor.execute(query)
        result = cursor.fetchall()
        courses = [list(course) for course in result]
        return courses


    def createNew(self):
        query = f'''
            INSERT INTO course (
                code,
                name,
                college
            )
            VALUES (
                '{self.code}',
                '{self.name}',
                '{self.college}'
            )
        '''
        cursor.execute(query)
        db.commit()
    

    @staticmethod
    def delete(code=None):
        query = f'''
            DELETE FROM course
            WHERE code='{code}'
        '''
        cursor.execute(query)
        db.commit()


    def update(self):
        query = f'''
            UPDATE course
            SET 
                code = '{self.code}',
                name = '{self.name}',
                college = '{self.college}'
            WHERE
                code = '{self.code}'
        '''
        cursor.execute(query)
        db.commit()


    @staticmethod
    def collegeCode(course_name):
        query = f'''
            SELECT course.name, college.code
            FROM course
            JOIN college
            ON course.college = college.code
            WHERE course.name = '{course_name}'
            LIMIT 1
        '''
        cursor.execute(query)
        _, collegecode = cursor.fetchone()
        return collegecode


    @staticmethod
    def courseCode(course_name):
        query = f'''
            SELECT code
            FROM course
            WHERE name = '{course_name}'
        '''
        cursor.execute(query)
        coursecode = cursor.fetchone()
        return coursecode[0]
