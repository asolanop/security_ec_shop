#!/usr/local/bin/python3

import Helpers.myparser as parser
import Helpers.db as db
import os, sys

print("Content-Type: text/html")

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
	print(login_form)

if os.getenv("REQUEST_METHOD") == 'POST':
	post_params = sys.stdin.read()
	log_intent = parser.parseData(post_params)
	db.connectDB()
	res = db.login(log_intent['username'],log_intent['password'])
	if res != None :
		print("Set-Cookie: SessionID=" + res['sessionID'] + ";")
		print("Set-Cookie: Expires=" + res['expiration'] + ";")
		print("Location: http://localhost/cgi-bin/MA-Shop/security_ec_shop/register.py")
		print()
		
		#print("Set-Cookie: sessionid=" + res[] + ";")
	else:
		print()
		print(login_form)
		print("""\
		
				<p style="color:red">Error de autenticaci&oacute;n, 
				por favor intente de nuevo.</p>
				""")
