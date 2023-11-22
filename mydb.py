import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost', 
    user = 'root',
    passwd = 'Toxic2304###',    
)

# Prepare a cursor to object
cursorObject = dataBase.cursor()

# Create a database connection
cursorObject.execute("CREATE DATABASE Calories")

print("All Done!")