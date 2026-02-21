import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sravani@01",
    database="fastapi_db"
)

cursor = conn.cursor(dictionary=True)