import mysql.connector as mysql


db = mysql.connect(
            host = 'localhost',
            user = 'root',
            password = 'edenrose',
            database = 'ssisdb'
        )
cursor = db.cursor()


def registeredUser(username,password):
        query = f'''
        SELECT username, password 
        FROM admin
        WHERE username = '{username}' and password = '{password}';
        '''
        cursor.execute(query)
        admin = cursor.fetchone()
        if admin:
            return True

