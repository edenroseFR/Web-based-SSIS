import mysql.connector as mysql
from os import getenv

db = mysql.connect(
            host = getenv('DB_HOST'),
            user = getenv('DB_USERNAME'),
            password = getenv('DB_PASSWORD'),
            database = getenv('DB_NAME')
            # host = 'us-cdbr-east-04.cleardb.com',
            # user = 'b0b5e5ffe03874',
            # password = '971dad9f',
            # database = 'heroku_7cab8ea6c6ec62e'
        )
cursor = db.cursor()



