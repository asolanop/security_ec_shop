#!/usr/bin/python3
import pymysql

global_conn = 0;

# Connect to the DB
def connectDB(): 
	print("Connecting to DB Mercadito")
	global global_conn 
	global_conn = getConection()
	print("You are now connected to Mercadito")
	init()

def getConection():
	conn = pymysql.connect(
	    db='mercadito',
	    user='root',
	    passwd='grisiru',
	    host='localhost')
	return conn

def init():
	# deleteData()
	insertSampleUsers()
	insertSampleItems()
	printData()

# Commit changes
def commitChanges():
	global_conn.commit()

# Delete all data from the DB
def deleteData():
	c = global_conn.cursor()	
	c.execute("DELETE FROM Users")
	c.execute("DELETE FROM Items")	
	commitChanges()

# Insert user
def insertUser(id,firstname,lastname,email,pw, username, phone, address):
	print("Inserting user")
	c = global_conn.cursor()	
	c.execute("INSERT INTO Users VALUES (null, %s, %s, %s, %s, %s, %s, %s)", (firstname, lastname, email, pw, username, phone, address))
	commitChanges()

# Insert item
def insertItem(id,name,price,descrip,owner):
	print("Inserting item")
	c = global_conn.cursor()	
	c.execute("INSERT INTO Items VALUES (null, %s, %s, %s, %s)", (name,price,descrip,owner))
	commitChanges()

# Print contents 
def printData():
	sql = "SELECT * FROM `Users` WHERE `email`=%s"
	c = global_conn.cursor()	
	c.execute(sql, ('mich@gmail.com'))
	result = c.fetchone()
	print(result)

# Insert sample data users
def insertSampleUsers():
	insertUser(1,"Michelle","Cersosimo","mich@gmail.com","password1","mich",22295015,"Coronado")
	insertUser(2,"Andres","Solano","andru@gmail.com","password2","andru",22829829,"Alajuela")

# Insert sample data items
def insertSampleItems():
	insertItem(1,"Maracas",2000.00,"pa cumbiar",1)
	insertItem(2,"Flauta Traversa",540.00,"fancy as it sounds",2)


