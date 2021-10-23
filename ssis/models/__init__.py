import mysql.connector as mysql


db = mysql.connect(
            host = 'us-cdbr-east-04.cleardb.com',
            user = 'b0b5e5ffe03874',
            password = '971dad9f',
            database = ''
        )
cursor = db.cursor()

