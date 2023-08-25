import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '1102'

)

cursor = database.cursor()

cursor.execute('CREATE DATABASE CRM')

print("Database created")