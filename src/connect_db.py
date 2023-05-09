import os
from dotenv import load_dotenv
import mysql.connector

# Load environment variables
load_dotenv("/home/javier/Universidad/Master/2º Semestre/Biological databases/.env")

# Get MySQL username and password from environment variables
user = os.environ.get("MYSQL_USER")
password = os.environ.get("MYSQL_PASSWORD")


# Establish connection
db = mysql.connector.connect(
    host="localhost",
    user=user,
    password=password,
    database="master_app"
)

# Execute SQL query
cursor = db.cursor()
cursor.execute("SELECT * FROM universities")
rows = cursor.fetchall()

# Print results
for row in rows[:20]:
    print(row)



