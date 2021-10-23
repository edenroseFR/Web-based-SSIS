from . import cursor, db

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
            USE heroku_7cab8ea6c6ec62e;
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
            USE heroku_7cab8ea6c6ec62e;
            SELECT username
            FROM admin
        '''
        cursor.execute(query)
        result = cursor.fetchall()
        usernames = [name[0] for name in result]

        return usernames

    
    def registered_user(self) -> bool:
        query = f'''
            USE heroku_7cab8ea6c6ec62e;
            SELECT username, password 
            FROM admin
            WHERE username = '{self.username}' and password = '{self.password}';
        '''
        cursor.execute(query)
        admin = cursor.fetchone()
        if admin:
            return True

