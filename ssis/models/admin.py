from . import cursor, db
from werkzeug.security import check_password_hash

class Admin():
    def __init__(
        self,
        username: str = None,
        password: str = None,
        password2: str = None) -> None:

        self.username = username
        self.password = password
        self.password2 = password2
    
    def register(self) -> None:
        query = f'''
            INSERT INTO admin(username, password)
            VALUE('{self.username}',
                  '{self.password}')
        '''
        cursor.execute(query)
        db.commit()
        return

    @staticmethod
    def get_usernames() -> list:
        query = f'''
            SELECT username
            FROM admin
        '''
        cursor.execute(query)
        result = cursor.fetchall()
        usernames = [name[0] for name in result]

        return usernames

    
    def registered_user(self) -> bool:
        query = f'''
            SELECT username, password 
            FROM admin
            WHERE username = '{self.username}';
        '''
        cursor.execute(query)
        username, password = cursor.fetchone()
        if username:
            if check_password_hash(password, self.password):
                return True

