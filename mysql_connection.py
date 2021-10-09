import mysql.connector as mysql


db = mysql.connect(
            host = 'localhost',
            user = 'root',
            password = 'edenrose',
            database = 'ssisdb'
        )
cursor = db.cursor()