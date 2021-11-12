from . import cursor, db

class Course():
    def __init__(
        self, 
        code: str = None,
        name: str = None,
        college: str = None,) -> None:
        
        self.code = code
        self.name = name
        self.college = college
    

    def get_all(self, page_num: int = None, item_per_page: int = None, paginate: bool = True) -> list:
        if not paginate:
            return self.course_list()
        offset = (page_num - 1) * item_per_page
        query = f'''
            SELECT course.code, course.name, course.college, college.name
            FROM course
            JOIN college
            ON course.college = college.code
            LIMIT {item_per_page} OFFSET {offset}
        '''
        cursor.execute(query)
        result = cursor.fetchall()
        courses = [list(course) for course in result]
        return courses

    
    @staticmethod
    def get_total() -> int:
        query = '''SELECT * FROM course'''
        cursor.execute(query)
        result = cursor.fetchall()
        total = len(result)
        return total


    @staticmethod
    def course_list() -> list:
        query = f'''
            SELECT course.code, course.name, course.college, college.name
            FROM course
            JOIN college
            ON course.college = college.code
        '''
        cursor.execute(query)
        result = cursor.fetchall()
        courses = [list(course) for course in result]
        return courses


    def search(self, keyword: str = None, field: str = None) -> list:
        keyword = keyword.upper()
        courses = self.get_all(paginate=False)
        result = []

        if field is None: 
            result = self.search_by_field(courses, keyword, 'all')
        elif field == 'code':
            result = self.search_by_field(courses, keyword, 'code')
        elif field == 'name':
            result = self.search_by_field(courses, keyword, 'name')
        elif field == 'college':
            result = self.search_by_field(courses, keyword, 'college')

        return result


    @staticmethod
    def search_by_field(rows: list = None, keyword: str = None, field: str = None) -> list:
        result = []
        for row in rows:
            row_allcaps = [str(cell).upper() for cell in row if cell != '']

            if field == 'all':
                if keyword in row_allcaps:
                    result.append(row)
            if field == 'code':
                if keyword in row_allcaps[0]:
                    result.append(row)
            elif field == 'name':
                if keyword in row_allcaps[1]:
                    result.append(row)
            elif field == 'college':
                if keyword in row_allcaps[2]:
                    result.append(row)

        return result


    @staticmethod
    def get_coursecodes() -> list:
        query = '''
            SELECT code
            FROM course
        '''
        cursor.execute(query)
        result = cursor.fetchall()
        CODES = [code[0] for code in result]
        return CODES


    @staticmethod
    def get_coursecode_for(course_name: str = None) -> str:
        query = f'''
                SELECT code
                FROM course
                WHERE name = '{course_name}'
            '''
        cursor.execute(query)
        coursecode = cursor.fetchone()
        return coursecode[0]


    def add_new(self) -> None:
        query = f'''
            INSERT INTO course (
                code,
                name,
                college)
            VALUES (
                '{self.code}',
                '{self.name}',
                '{self.college}')
        '''
        cursor.execute(query)
        db.commit()
        return None
    

    @staticmethod
    def delete(code: str = None) -> None:
        query = f'''
            DELETE FROM course
            WHERE code='{code}'
        '''
        cursor.execute(query)
        db.commit()
        return None


    def update(self) -> None:
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
    def get_collegecode(course_name: str = None) -> str:
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


