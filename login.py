#!/usr/bin/python3

import Helpers.structure as structure
import Helpers.nav as nav
import Helpers.myparser as parser
import Helpers.validator as validator
import Helpers.db as db
import os, sys


db.connectDB()
cookie = parser.parseCookie(os.getenv("HTTP_COOKIE"))
autenticate = db.checkSession(parser.parseCookie(os.getenv("HTTP_COOKIE"))) if validator.validateSession(cookie) else None
if autenticate == None :		
	login_form = """\
	<div>
	<h2>Enter your credentials to login:</h2>
	<form method="POST">
		<label for="username">Username: </label>
		<input id="username" name="username" maxlength="25" />
		<br />
		<label for="password">Password: </label>
		<input id="password" name="password" maxlength="25" type="password" />
		<br />
		<button>Login</button>
	</form></div>"""
	
	if os.getenv("REQUEST_METHOD") == 'GET':
		print("Content-Type: text/html;\r\n\r\n")
		structure.printStartSection()
		nav.printNav(None)	
		print(login_form)

	if os.getenv("REQUEST_METHOD") == 'POST':
		post_params = sys.stdin.read()
		login_intent = parser.parseData(post_params)
		validation = validator.validateLogin(login_intent)
		if validation == False :
			print("Content-Type: text/html;\r\n\r\n")
			structure.printStartSection()
			nav.printNav(None)	
			print(login_form)
			print("""\<p style="color:red">Authentication error, try again</p>""")
		else :
			db.connectDB()
			res = db.login(login_intent['username'],login_intent['password'])
			if res != None :
				if res != -1 :
					print("Set-Cookie: SessionID=" + res['sessionID'] + ";")
					print("Set-Cookie: Expires=" + res['expiration'] + ";")
					#print("Location: http://localhost/cgi-bin/MA-Shop/security_ec_shop/index.py")
					print("Location: https://172.24.129.8//index.py")
					print()
				else :
					print("Content-Type: text/html;\r\n\r\n")
					structure.printStartSection()
					nav.printNav(None)	
					print(login_form)
					print("""<p style="color:red">Your user has been blocked. Contact site's admin to unblock it!</p>""")
			else:
				print("Content-Type: text/html;\r\n\r\n")
				structure.printStartSection()
				nav.printNav(None)	
				print(login_form)
				print("""\<p style="color:red">Authentication error, try again</p>""")
else :
	#print("Location: http://localhost/cgi-bin/MA-Shop/security_ec_shop/index.py;")	
	print("Location: https://172.24.129.8/index.py")
	print()
