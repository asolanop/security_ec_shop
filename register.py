#!/usr/local/bin/python3

import Helpers.myparser as parser
import Helpers.db as db
import os, sys
import Helpers.structure as structure
import Helpers.nav as nav

if os.getenv("REQUEST_METHOD") == 'GET': 
	print("Content-Type: text/html")
	print()
	structure.printStartSection()
	nav.printNav(None)		
	print ("""\

<div>
	<h3>Please complete the data below:</h3>
	<div id=divregister>	
	<form method="POST">
		<label for="firstname">Name*: </label>
		<br />
		<input id="firstname" name="firstname" maxlength="50" type="text" />
		<br />
		<label for="lastname">Last Name*: </label>
		<br />
		<input id="lastname" name="lastname" maxlength="50" type="text" />
		<br />
		<label for="username">Username*: </label>
		<br />
		<input id="username" name="username" maxlength="25" type="text"/>
		<br />
		<label for="password">Password*: </label>
		<br />
		<input id="password" name="password" maxlength="25" type="password" />
		<br />
		<label for="email">Email*: </label>
		<br />
		<input id="email" name="email" maxlength="50" type="email" />
		<br />
		<label for="address">Address*: </label>
		<br />
		<input id="address" name="address" maxlength="50" />
		<br />
		<label for="telephone">Phone*: </label>
		<br />
		<input id="telephone" name="telephone" maxlength="10" type="number" />
		<br />
		<button>Submit</button>
	</form>
	</div>
</div>""")

if os.getenv("REQUEST_METHOD") == 'POST':
	post_params = sys.stdin.read()
	user = parser.parseData(post_params)
	db.connectDB()
	db.insertUser("id", user['firstname'], user['lastname'], user['email'], 
				user['password'], user['username'], user['telephone'], user['address'])
	
	print("Content-Type: text/html")
	print()
	print ("""\

<div>
	<h2>User added succesfully: <a href="login.py">Clic to login</a></h2>
""")
	

