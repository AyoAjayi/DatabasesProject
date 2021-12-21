# from application import db

import mysql.connector
#replace the username and password to that of your db. Comment out this line and don't delete it for my db.


mydb = mysql.connector.connect(host="localhost", user="root", password="cool1234", database="mydb")
mycursor = mydb.cursor()
# mycursor.execute("show databases")
mycursor.callproc('sp_createUser')
mycursor.execute("select country_name from country")

#this will print out all databases
for i in mycursor:
    print(i)

#when we start making procedures
#cursor.callproc()
# cursor.callproc('sp_createUser',(_name,_email,_hashed_password))