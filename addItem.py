#!/usr/bin/python3.6

import Helpers.myparser as parser
import Helpers.db as db
import os, sys
import Helpers.structure as structure
import Helpers.nav as nav

db.connectDB()
autenticate = db.checkSession(parser.parseCookie(os.getenv("HTTP_COOKIE")))
if autenticate == None :
	#print("Location: http://localhost/cgi-bin/MA-Shop/security_ec_shop/login.py")
	print("Location: http://localhost/login.py")
	print()

else :	
	# Form to get item data 
	print("Content-Type: text/html\r\n\r\n")
	structure.printStartSection()
	nav.printNav(autenticate, db.cartCount(autenticate))
	print ("""<div>
		<h3>Enter your product information:</h3>
		<form method="POST">
		<label for="name">Item Name*: </label>
		<input id="name" name="name" maxlength="50" /><br />
		<label for="description">Description*: </label>
		<input id="description" name="description" 
			maxlength="50" /><br />
		<label for="price">Price*: </label>
		<input id="price" name="price" 
			maxlength="25" type="number" /><br />
		<button>Submit</button>
		</form></div>""")

	# Post method 
	if os.getenv("REQUEST_METHOD") == 'POST':
		post_params = sys.stdin.read()	
		item = parser.parseData(post_params)
		db.connectDB()
		# Insert into DB Items
		db.insertItem("id", item['name'], item['price'], item['description'], autenticate)
		print ("""\<div>
		<h2>Item added succesfully! 
		<a href="index.py">Go back to Home</a></h2>""")
	
