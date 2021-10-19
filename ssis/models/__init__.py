import mysql.connector as mysql
import os

db = mysql.connect(
            host = os.environ.get('LOCAL_HOST'),
            user = os.environ.get('DB_USER'),
            password = os.environ.get('DB_PASSWORD'),
            database = os.environ.get('DB_NAME')
        )
cursor = db.cursor()
