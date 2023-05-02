import mysql.connector

#connection to mysql
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Adarsh@1",
    database="resensys"
)

#creating a variable to connect to the sql
cursor = mydb.cursor()

#uses the database resensys
cursor.execute("use resensys")

#creates a new table with the following parameters
cursor.execute("CREATE TABLE resensysProducts(barcodeID int, productName varchar(255), productDetails varchar(255), manufacturingDate varchar(255))")

#deletes all the values from the table, if there were any from a previous run
cursor.execute("truncate resensysProducts")

#data creation
cursor.execute("insert into resensysProducts(barcodeID, productName, productDetails, manufacturingDate)"
               "values (0000000001, \"SenSpot\", \"attached to structure\", \"12/22/19\")")

cursor.execute("insert into resensysProducts(barcodeID, productName, productDetails, manufacturingDate)"
               "values (0000000002, \"SeniMax\", \"collects SenSpot data on site and sends to remote structure\", \"7/05/20\")")

cursor.execute("insert into resensysProducts(barcodeID, productName, productDetails, manufacturingDate)"
               "values (0000000003, \"SenScope\", \"software package that analyzes data and generates alerts\", \"4/12/20\")")

cursor.execute("insert into resensysProducts(barcodeID, productName, productDetails, manufacturingDate)"
               "values (0000000004, \"SenSpot\", \"attached to structure\", \"12/22/19\")")


#read data
cursor.execute("SELECT * FROM resensysProducts")

output = cursor.fetchall()

for x in output:
   print(x)


#data deletion
print("\nAnything part of Senspot was removed. Check Below\n")

cursor.execute("set sql_safe_updates = 0")

cursor.execute("delete from resensysProducts where productName = \'SenSpot\'")

cursor.execute("SELECT * FROM resensysProducts")

output = cursor.fetchall()

for x in output:
    print(x)


#data update
print("\nAnything containing \"Sen\" was updated to be Senspot\n")

cursor.execute("set sql_safe_updates = 0")

cursor.execute("update resensysProducts set productName = \'Senspot\' where productName like \'%Sen%\'")

cursor.execute("SELECT * FROM resensysProducts")

output = cursor.fetchall()

for x in output:
    print(x)

#deletes the entire table
cursor.execute("drop table resensysProducts")

#sets the mode to not be able to delete any more data (safety precaution)
cursor.execute("set sql_safe_updates = 1")
