from . import cursor, db

class College():
    def __init__(
        self, 
        code: str = None,
        name: str = None) -> None:
        
        self.code = code
        self.name = name
    

    def get_all(self) -> list:
        query = '''
            SELECT code, name
            FROM college;
        '''
        cursor.execute(query)
        result = cursor.fetchall()
        colleges = [list(college) for college in result]
        return colleges

    
    def get_statistics(self) -> list:
        colleges = self.get_all()
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
    def get_departments() -> list:
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


    def search(self, keyword: str = None, field: str = None) -> list:
        keyword = keyword.upper()
        colleges = self.get_statistics()
        result = []

        if field is None: 
            result = self.search_by_field(colleges, keyword, 'all')
        elif field == 'code':
            result = self.search_by_field(colleges, keyword, 'code')
        elif field == 'name':
            result = self.search_by_field(colleges, keyword, 'name')
        elif field == 'coursecount':
            result = self.search_by_field(colleges, keyword, 'coursecount')
        elif field == 'studentcount':
            result = self.search_by_field(colleges, keyword, 'studentcount')

        return result


    @staticmethod
    def search_by_field(rows: list = None, keyword: str = None, field: str = None) -> list:
        result = []
        for row in rows:
            row_allcaps = [str(cell).upper() for cell in row]

            if field == 'all':
                if keyword in row_allcaps:
                    result.append(row)
            if field == 'code':
                if keyword == row_allcaps[0]:
                    result.append(row)
                    return result
            elif field == 'name':
                if keyword == row_allcaps[1]:
                    result.append(row)
            elif field == 'coursecount':
                if keyword in row_allcaps[2]:
                    result.append(row)
            elif field == 'studentcount':
                if keyword in row_allcaps[3]:
                    result.append(row)

        return result


    def add_new(self) -> None:
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
        return None
    

    @staticmethod
    def delete(code: str = None) -> None:
        query = f'''
            DELETE FROM college
            WHERE code='{code}'
        '''
        cursor.execute(query)
        db.commit()
        return None


    def update(self) -> None:
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
        return None


    @staticmethod
    def get_collegecode_for(course_name: str = None) -> str:
        query = f'''
            SELECT code
            FROM college
            WHERE name = '{course_name}'
        '''
        cursor.execute(query)
        code = cursor.fetchone()[0]
        return code


    @staticmethod
    def get_collegecodes() -> list:
        query = '''
            SELECT code
            FROM college
        '''
        cursor.execute(query)
        result = cursor.fetchall()
        CODES = [code[0] for code in result]
        return CODES



