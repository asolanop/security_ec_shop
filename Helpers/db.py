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
	c.execute("INSERT INTO Users (id, first_name, last_name, email, password, username, telephone, address) VALUES (null, %s, %s, %s, %s, %s, %s, %s)", (firstname, lastname, email, pw, username, phone, address))
	createUserCart(c.lastrowid)
	commitChanges()

# Is Admin or not 
def isAdmin(user_id):
	try :
		sql = "Select role FROM Users where id=%s"
		c = global_conn.cursor()
		c.execute(sql, (user_id))
		data = c.fetchone()
		return data[0]
	except:
		return None


# Create a cart tuple for a just created user
def createUserCart(user_id):
	try :
		sql = "Insert INTO Cart Values(null, %s)"
		c = global_conn.cursor()
		c.execute(sql, (int(user_id)))
		commitChanges()
	except :
		return None

# Get cart items count
def cartCount(user_id):
	try :
		cart_id = getUserCart(user_id)
		sql = "Select COUNT(item_id) FROM Cart_Items where cart_id=%s"
		c = global_conn.cursor()
		c.execute(sql, (cart_id))
		data = c.fetchone()
		return data[0]
	except:
		return None

def clearCart(user_id):
	cart_id = getUserCart(user_id)
	sql = "Delete From Cart_Items where cart_id=%s"
	c = global_conn.cursor()
	c.execute(sql,(cart_id))
	commitChanges()

def getCartItems(user_id):
	cart_id = getUserCart(user_id)
	sql = "Select Items.name, Items.description, Items.price, Items.id from Cart_Items join Items on item_id = id where cart_id=%s ;"
	c = global_conn.cursor()
	c.execute(sql,(cart_id))
	data = c.fetchall()
	return data

# Insert item
def insertItem(id, name, price, description, owner):
	c = global_conn.cursor()	
	c.execute("INSERT INTO Items VALUES (null, %s, %s, %s, %s)", (name, price, description, owner))
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
	c = global_conn.cursor()	
	c.execute("INSERT INTO Users VALUES (null, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", ("Michelle","Cersosimo","mich@zoquetemail.com","admin","mich",22295015,"Coronado", 1, 0, 1))
	createUserCart(c.lastrowid)
	c.execute("INSERT INTO Users VALUES (null, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",("Andres","Solano","andru@zoquetemail.com","admin","andru",22829829,"Alajuela", 1, 0, 1))
	createUserCart(c.lastrowid)
	commitChanges()

# Insert sample data items
def insertSampleItems():
	insertItem(1,"La Maraca",2000.00,"Sabores dulces con una pizca de maracuya",1)
	insertItem(2,"Domingo 7 ",1540.00,"Para esos dias especiales, nuestra combinacion IPA oscura",2)
	insertItem(3,"Lagarta",1700.00,"Fria como ella sola, nuestros citricos cerveceros combinan perfecto con esta solucion amarga",2)

def getAllItems():
	c = global_conn.cursor()	
	c.execute("SELECT name, price, description, id FROM Items")
	data = c.fetchall()
	return data

def search(searchby): 
	c = global_conn.cursor()	
	c.execute("SELECT name, price, description, id FROM Items where name LIKE '%"+searchby+"%' OR description LIKE'%"+searchby+"%';")
	data = c.fetchall()
	return data

def getUserCart(user_id):
	sql = "Select id FROM `Cart` WHERE user_id=%s;"
	try : 
		c = global_conn.cursor()
		c.execute(sql, (user_id))
		if c.rowcount > 0:
			data = c.fetchone()
			return data[0]
		else:
			return None
	except :
		return None

def addToCart(item_id, user_id):
	sql = "INSERT INTO Cart_Items VALUES (%s, %s, 1);"
	cart_id = getUserCart(user_id)
	if cart_id == None :
		return None
	try :
		c = global_conn.cursor()
		c.execute(sql, (cart_id, int(item_id)))
		commitChanges()
		return 1
	except :
		None

def login(username, password):
	sql = "call login(%s, %s); "
	c = global_conn.cursor()
	c.execute(sql, (username, password))
	data = c.fetchall()
	result = data[0][0]
	if result != None :
		if result != -1 :
			return createSession(data)
		else :
			return -1
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
		return {'sessionID':random_key,'expiration':expiration_date.strftime('%a, %d %b %Y %T GMT')}
	except :
		return None

def checkSession(sessionCookie):
	if sessionCookie != None :
		if 'SessionID' in sessionCookie :
			sql = "SELECT user_id FROM `Sessions` WHERE `id`=%s AND `expiration`>NOW();"
			try :
				c = global_conn.cursor()
				c.execute(sql, (sessionCookie['SessionID']))
				if c.rowcount > 0:
					data = c.fetchone()
					return data[0]
			except :
				#print("Error checking cookie on DB")
				return None
	return None

def delSession(sessionCookie):
	sql = "Delete FROM `Sessions` WHERE `id`=%s;"
	try:
		c = global_conn.cursor()
		c.execute(sql, (sessionCookie))
		commitChanges()
		return 1
	except:
		return None
