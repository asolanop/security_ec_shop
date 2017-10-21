#!/usr/local/bin/python3

import Helpers.myparser as parser
import Helpers.db as db
import os, sys

db.connectDB()
autenticate = db.checkSession(parser.parseCookie(os.getenv("HTTP_COOKIE")))
if autenticate != None :
	print("Location: http://localhost/cgi-bin/MA-Shop/security_ec_shop/index.py")
	print()

else :	

	login_form = """\

<div>
	<h2>Ingrese sus datos de autenticaci&oacute;n:</h2>
	<form method="POST">
		<label for="username">Nombre de usuario: </label>
		<input id="username" name="username" maxlength="25" />
		<br />
		<label for="password">Contrasena: </label>
		<input id="password" name="password" maxlength="25" type="password" />
		<br />
		<button>Iniciar sesi&oacute;n</button>
	</form>
</div>

"""
	
	if os.getenv("REQUEST_METHOD") == 'GET':
		print()
		print(login_form)

	if os.getenv("REQUEST_METHOD") == 'POST':
		post_params = sys.stdin.read()
		log_intent = parser.parseData(post_params)
		db.connectDB()
		res = db.login(log_intent['username'],log_intent['password'])
		if res != None :
			print("Set-Cookie: SessionID=" + res['sessionID'] + ";")
			print("Set-Cookie: Expires=" + res['expiration'] + ";")
			print("Location: http://localhost/cgi-bin/MA-Shop/security_ec_shop/index.py")
			print()
		else:
			print()
			print(login_form)
			print("""\	
				<p style="color:red">Error de autenticaci&oacute;n, 
				por favor intente de nuevo.</p>
				""")
