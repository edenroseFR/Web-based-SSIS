from mysql_connection import cursor, db

class Admin():
    def __init__(
        self,
        username=None,
        password=None,
        password2=None
    ):

        self.username = username
        self.password = password
        self.password2 = password2
    
    def register(self):
        query = f'''
            INSERT INTO admin(username, password)
            VALUE('{self.username}',
                    '{self.password}')
        '''
        cursor.execute(query)
        db.commit()
        return

    @staticmethod
    def existingUsernames():
        query = f'''
            SELECT username
            FROM admin
        '''
        cursor.execute(query)
        result = cursor.fetchall()
        usernames = [name[0] for name in result]

        return usernames
    
    def registeredUser(self):
        query = f'''
        SELECT username, password 
        FROM admin
        WHERE username = '{self.username}' and password = '{self.password}';
    '''
        cursor.execute(query)
        admin = cursor.fetchone()
        if admin:
            return True

