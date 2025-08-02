import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()
db_config = {
    "host":os.getenv("YOUR_HOST_NAME"),
    "user":os.getenv("YOUR_USER_NAME"),
    "password":os.getenv("YOUR_PASSWORD"),
    "database":os.getenv("YOUR_DATABASE")
}


#For Other Database
# MYSQL: Use mysql.connector
# PostgreSQL: Use psycopg2
# SQL Server: Use pyodbc
# SQLite: Use sqlite3


conn = psycopg2.connect(**db_config)
cursor = conn.cursor()
# you can enter your query here
query = "SELECT first_name,last_name AS Name FROM ACTOR WHERE first_name = 'JENNIFER';"
cursor.execute(query=query)
result = cursor.fetchall()

for row in result:
    print(row)