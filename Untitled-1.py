import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="company")

mycursor = mydb.cursor()

query = "insert into employee(id,name,salary) values(%s,%s,%s)",(4,"kali",27000)
#query= "select * from employee"

mycursor.execute(query)

for (user_name) in mycursor:
    print(user_name)