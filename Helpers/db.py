#!/usr/local/bin/python3
import pymysql, os, hashlib, time
from datetime import datetime, timedelta

global_conn = 0;

def init():
	connectDB()
	deleteData()
	insertSampleUsers()
	insertSampleItems()
	#printData()

# Connect to the DB
def connectDB(): 
	#print("Connecting to DB Mercadito")
	global global_conn 
	global_conn = getConection()
	#print("You are now connected to Mercadito")

def getConection():
	conn = pymysql.connect(
	    db='mercadito',
	    user='root',
	    passwd='',
	    host='localhost')
	return conn

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
	#print("Inserting user")
	c = global_conn.cursor()	
	c.execute("INSERT INTO Users VALUES (null, %s, %s, %s, %s, %s, %s, %s)", (firstname, lastname, email, pw, username, phone, address))
	commitChanges()

# Insert item
def insertItem(id,name,price,descrip,owner):
	#print("Inserting item")
	c = global_conn.cursor()	
	c.execute("INSERT INTO Items VALUES (null, %s, %s, %s, %s)", (name,price,descrip,owner))
	commitChanges()

# Print contents 
def printData():
	sql = "SELECT * FROM `Users` WHERE `email`=%s"
	c = global_conn.cursor()	
	c.execute(sql, ('mich@zoquetemail.com'))
	result = c.fetchone()
	print(result)

# Insert sample data users
def insertSampleUsers():
	insertUser(1,"Michelle","Cersosimo","mich@zoquetemail.com","password1","mich",22295015,"Coronado")
	insertUser(2,"Andres","Solano","andru@zoquetemail.com","password2","andru",22829829,"Alajuela")

# Insert sample data items
def insertSampleItems():
	insertItem(1,"Maracas",2000.00,"pa cumbiar",1)
	insertItem(2,"Flauta Traversa",540.00,"fancy as it sounds",2)

def getAllItems():
	c = global_conn.cursor()	
	c.execute("SELECT name, price, description FROM Items")
	data = c.fetchall()
	return data

def login(username, password):
	sql = "SELECT * FROM `Users` WHERE `username`=%s AND `password`=%s;"
	c = global_conn.cursor()
	c.execute(sql, (username, password))
	if c.rowcount > 0:
		data = c.fetchone()
		return createSession(data)
	else:
		return None

def createSession(log_intent):
	random_data = os.urandom(128)
	random_key = hashlib.md5(random_data).hexdigest()
	start_date = time.strftime('%Y-%m-%d %H:%M:%S')
	date_created = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
	expiration_date = date_created+timedelta(days=1)
	try:
		c = global_conn.cursor()
		c.execute("INSERT INTO Sessions VALUES (%s, %s, %s, %s)", (random_key,date_created,expiration_date,log_intent[0]))
		commitChanges()
		return {'sessionID':random_key,'expiration':expiration_date.strftime('%Y-%m-%d %H:%M:%S')}
	except :
		return None
