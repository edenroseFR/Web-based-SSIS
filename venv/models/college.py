from mysql_connection import cursor, db

class College():
    def __init__(
        self, 
        code=None,
        name=None):
        
        self.code = code
        self.name = name
    

    def showAll(self):
        query = '''
            SELECT code, name
            FROM college;
        '''
        cursor.execute(query)
        result = cursor.fetchall()
        colleges = [list(college) for college in result]
        return colleges

    
    def statistics(self):
        colleges = self.showAll()
        query = '''
            SELECT college.code, college.name, COUNT(*) AS courses, enrolled.student as enrolled
            FROM college
            JOIN course
            ON college.code = course.college
            LEFT JOIN (SELECT collegecode, COUNT(*) as student
                        FROM students
                        GROUP BY collegecode) enrolled
            ON college.code = enrolled.collegecode
            GROUP BY college.code
        '''
        cursor.execute(query)
        result = cursor.fetchall()
        stat = [list(college) for college in result]

        for college in colleges:
            if college[0] not in [code[0] for code in stat]:
                stat.append([college[0], college[1], None, None])
        
        return stat


    @staticmethod
    def departments():
        query = '''
            SELECT college.code, course.name
            FROM college
            JOIN course
            ON college.code = course.college
        '''
        cursor.execute(query)
        result = cursor.fetchall()
        departments = [list(department) for department in result]
        return departments


    def search(self, keyword=None):
        keyword = keyword.upper()
        colleges = self.statistics()
        result = []

        for college in colleges:
            college_allcaps = [str(info).upper() for info in college]
            if keyword in college_allcaps:
                result.append(college)
        return result


    def addNew(self):
        query = f'''
            INSERT INTO college (
                code,
                name
            )
            VALUES (
                '{self.code}',
                '{self.name}'
            )
        '''
        cursor.execute(query)
        db.commit()
    

    @staticmethod
    def delete(code=None):
        query = f'''
            DELETE FROM college
            WHERE code='{code}'
        '''
        cursor.execute(query)
        db.commit()


    def update(self):
        query = f'''
            UPDATE college
            SET 
                code = '{self.code}',
                name = '{self.name}'
            WHERE
                code = '{self.code}'
        '''
        cursor.execute(query)
        db.commit()


    @staticmethod
    def collegeCode(course_name=None):
        query = f'''
            SELECT code
            FROM college
            WHERE name = '{course_name}'
        '''
        cursor.execute(query)
        code = cursor.fetchone()[0]
        return code


    @staticmethod
    def codeList():
        query = '''
            SELECT code
            FROM college
        '''
        cursor.execute(query)
        result = cursor.fetchall()
        CODES = [code[0] for code in result]
        return CODES



