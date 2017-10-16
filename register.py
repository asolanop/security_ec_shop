<<<<<<< HEAD
#!/usr/local/bin/python3
import Helpers.myparser as parser
import Helpers.db as db
=======
#!/usr/bin/python3

>>>>>>> 70e15bc139bafb029b15c5682a1e7b7911e422a3
import os, sys

if os.getenv("REQUEST_METHOD") == 'GET': 
	print("Content-Type: text/html")
	print()
	print ("""\

<div>
	<h2>Enter your data to register:</h2>
	<form method="POST">
		<label for="firstname">Nombre*: </label>
		<input id="firstname" name="firstname" maxlength="50" />
		<br />
		<label for="lastname">Apellido*: </label>
		<input id="lastname" name="lastname" maxlength="50" />
		<br />
		<label for="username">Nombre de usuario*: </label>
		<input id="username" name="username" maxlength="25" />
		<br />
		<label for="password">Contrasena*: </label>
		<input id="password" name="password" maxlength="25" type="password" />
		<br />
		<label for="email">Correo electr&oacute;nico*: </label>
		<input id="email" name="email" maxlength="50" type="email" />
		<br />
		<label for="address">Direcci&oacute;n*: </label>
		<input id="address" name="address" maxlength="50" />
		<br />
		<label for="telephone">Tel&eacute;fono*: </label>
		<input id="telephone" name="telephone" maxlength="10" type="number" />
		<br />
		<button>Submit</button>
	</form>
</div>

""")

if os.getenv("REQUEST_METHOD") == 'POST':
	post_params = sys.stdin.read()
	user = parser.parse(post_params)
	db.connectDB()
	db.insertUser("id", user['firstname'], user['lastname'], user['email'], 
				user['password'], user['username'], user['telephone'], user['address'])
	print("Location:http://localhost/")
	print()
	

