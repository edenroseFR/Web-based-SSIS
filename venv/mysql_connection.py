import mysql.connector as mysql


db = mysql.connect(
            host = 'localhost',
            user = 'root',
            password = 'edenrose',
            database = 'ssisdb'
        )
cursor = db.cursor()


def registeredUser(username=None ,password=None):
    query = f'''
        SELECT username, password 
        FROM admin
        WHERE username = '{username}' and password = '{password}';
    '''
    cursor.execute(query)
    admin = cursor.fetchone()
    if admin:
        return True


def existingUsernames():
    query = f'''
        SELECT username
        FROM admin
    '''
    cursor.execute(query)
    result = cursor.fetchall()
    usernames = [name[0] for name in result]

    return usernames


def registerAdmin(username=None, password=None):
    query = f'''
        INSERT INTO admin(username, password)
        VALUE('{username}', '{password}')
    '''
    cursor.execute(query)
    db.commit()

    return


def getStudents():
    query = f'''
        SELECT id, firstname, middlename, lastname, gender, year, coursecode, collegecode
        FROM students;
    '''
    cursor.execute(query)
    result = cursor.fetchall()
    students = [list(student) for student in result]
    
    return students

