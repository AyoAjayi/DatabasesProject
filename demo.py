import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="navin", passwd="1234")
mycursor = mydb.cursor()
mycursor.execute("show databases")