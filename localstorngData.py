# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='123456',
#     database='mytext'
# )
# mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM user")
# result = mycursor.fetchall()
# val = {
#     "name": "李思",
#     # "age": 12
# }
# sql = "INSERT INTO user (name, age) VALUES (%s, %s)"
# mycursor.execute(sql, list(val.values()))
#
# print(result)

import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='mytext'
)

mycursor = mydb.cursor()
print(mycursor)
# Define the values to be inserted
val = {
    "name": "李思",
    "age": 12
}

# Construct the SQL query with placeholders
sql = "INSERT INTO user (name, age) VALUES (%s, %s)"

# Execute the query with the values from the dictionary
mycursor.execute(sql, list(val.values()))

# Make changes to the database persistent
mydb.commit()
