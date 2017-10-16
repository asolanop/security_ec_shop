#!/usr/bin/python3

import os, sys

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

print(os.getenv("REQUEST_METHOD"))

from Helpers import myparser

myparser.a()

if os.getenv("REQUEST_METHOD") == 'POST':
	print("POSTING DATA")
	post_params = sys.stdin.read()
	user = parser.parse(post_params)
	print(user)

