import mysql.connector as mysql
from os import getenv

db = mysql.connect(
            host = getenv('DB_HOST'),
            user = getenv('DB_USERNAME'),
            password = getenv('DB_PASSWORD'),
            database = getenv('DB_NAME')
        )
cursor = db.cursor()



