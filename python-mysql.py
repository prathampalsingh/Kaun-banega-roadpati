import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="pysql"
    )
    mycursor = mydb.cursor()
    query= "select * from book"
    #query = "CREATE TABLE book(bid integer(4), title varchar(20), price integer(5))"
    #query = "insert book(bid,title,price) values(%s,%s,%s)"
    #b1 = (1,"sql",499)
    #list = [(2,"python",599),(3,"pysql",899),(4,"java",399)]
   # mycursor.executemany(query,list)
    #mydb.commit()
    #for (user_name) in mycursor:
    #    print(user_name)

    mycursor.execute(query)
    result = mycursor.fetchall()
    print(result)
    #for i in result:
    #     print(i)


    # Execute your SQL queries here using mycursor

except mysql.connector.Error as err:
    print("Error connecting to MySQL server:", err)

finally:
    if mydb.is_connected():
        mydb.close()
        print("Connection to MySQL server is closed")