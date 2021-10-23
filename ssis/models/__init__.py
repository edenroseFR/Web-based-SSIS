import mysql.connector as mysql


# db = mysql.connect(
#             host = 'us-cdbr-east-04.cleardb.com',
#             user = 'b0b5e5ffe03874',
#             password = '971dad9f',
#             database = 'heroku_7cab8ea6c6ec62e'
#         )
db = mysql.connect(
            host = 'localhost',
            user = 'root',
            password = 'edenrose',
            database = 'ssisdb'
        )
cursor = db.cursor()

