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


    def createNew(self):
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

