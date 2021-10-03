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
    

    def get_all(self):
        query = '''
            SELECT course.code, course.name, course.college, college.name
            FROM course
            JOIN college
            ON course.college = college.code
        '''
        cursor.execute(query)
        result = cursor.fetchall()
        courses = [list(course) for course in result]
        return courses


    def search(self, keyword=None):
        keyword = keyword.upper()
        courses = self.get_all()
        result = []

        for course in courses:
            course_allcaps = [str(info).upper() for info in course]
            if keyword in course_allcaps:
                result.append(course)
        return result


    @staticmethod
    def get_coursecodes():
        query = '''
            SELECT code
            FROM course
        '''
        cursor.execute(query)
        result = cursor.fetchall()
        CODES = [code[0] for code in result]
        return CODES


    @staticmethod
    def get_coursecode_for(course_name):
        query = f'''
                SELECT code
                FROM course
                WHERE name = '{course_name}'
            '''
        cursor.execute(query)
        coursecode = cursor.fetchone()
        return coursecode[0]


    def add_new(self):
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
        return None
    

    @staticmethod
    def delete(code=None):
        query = f'''
            DELETE FROM course
            WHERE code='{code}'
        '''
        cursor.execute(query)
        db.commit()
        return None


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
        return None


    @staticmethod
    def get_collegecode(course_name):
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


