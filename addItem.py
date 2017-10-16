#!/usr/bin/python3

import Helpers.myparser as parser
import Helpers.db as db
import os, sys

print("Content-Type: text/html\r\n\r\n")

# Form to get item data 
print ("""<div>
	<h2>Enter your product data:</h2>
	<form method="POST">
	<label for="name">Item Name*: </label>
	<input id="name" name="name" maxlength="50" /><br />
	<label for="description">Description*: </label>
	<input id="description" name="description" maxlength="50" /><br />
	<label for="price">Price*: </label>
	<input id="price" name="price" maxlength="25" type="number" /><br />
	<button>Submit</button>
	</form></div>""")

# Post method 
if os.getenv("REQUEST_METHOD") == 'POST':
	post_params = sys.stdin.read()	
	item = parser.parseData(post_params)
	db.connectDB()
	# Insert into DB Items
	db.insertItem("id", item['name'], item['price'], item['description'], 124)
	print ("""\<div>
	<h2>Item added succesfully! 
	<a href="index.py">Go back to Home</a></h2>""")
	
