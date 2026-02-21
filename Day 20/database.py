import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sravani@01",  # replace with your MySQL password
    database="fastapi_db"
)

cursor = conn.cursor(dictionary=True)