#!/usr/bin/python3


import Helpers.myparser as parser
import Helpers.db as db
import os, sys
import Helpers.structure as structure
import Helpers.nav as nav

db.connectDB()
autenticate = db.checkSession(parser.parseCookie(os.getenv("HTTP_COOKIE")))

# Form to get feedback data 
print("Content-Type: text/html\r\n\r\n")
structure.printStartSection()
nav.printNav(autenticate, db.cartCount(autenticate))
print ("""<div>
	<h3>Enter your feedback:</h3>
	<form id="commentForm" method="POST">

	<label for="email">Your email*: </label>
	<input id="email" name="email" maxlength="50" type="text" /><br />
	
	<label for="firstname">Name*: </label>
	<input id="firstname" name="firstname" maxlength="25" type="text" /><br />
	
	<label for="lastname">Lastname*: </label>
	<input id="lastname" name="lastname" maxlength="25" type="text" /><br />
	<br/>
	<label for="comment">Your comment/doubt/feedback*: </label>
	<br/><br/>
	<textarea name="comment" form="commentForm">Enter text here...</textarea>	<br/>	

	<button id="submit">Submit</button>
	</form>
	<br>
	
	</div>""")

# Post method 
if os.getenv("REQUEST_METHOD") == 'POST':
	post_params = sys.stdin.read()	
	feed = parser.parseData(post_params)
	db.connectDB()
	# Insert into DB Items
	#db.insertFeed("id", feed['comment'], feed['email'], feed['firstname'], feed['lastname'], autenticate)
	print ("""\<div>
	<h2>Your comment was added succesfully! 
	<a href="index.py">Go back to Home</a></h2>""")

