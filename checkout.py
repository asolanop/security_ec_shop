#!/usr/local/bin/python3

import Helpers.db as db
import Helpers.myparser as parser
import Helpers.structure as structure
import Helpers.nav as nav
import os, sys

db.connectDB()
autenticate = db.checkSession(parser.parseCookie(os.getenv("HTTP_COOKIE")))
if autenticate == None :
	print("Location: http://localhost/cgi-bin/MA-Shop/security_ec_shop/login.py")
	#print("Location: http://localhost/login.py")
	print()
else :
	print("Content-Type: text/html\r\n\r\n")
	structure.printStartSection()
	nav.printNav(autenticate, db.cartCount(autenticate))
	if os.getenv("REQUEST_METHOD") == 'GET':
		print("""\
			<div>
			<form method="POST"> 
				<label for="address">Enter the addres to deliver your items: </label>
				<input id="address" name="address" maxlength="25" type="text" />
				<button>Submit</button>
			</form>
			
			<p> Your items to be delivered: </p>
			</div>
	 	""")
		items = db.getCartItems(autenticate)

	if os.getenv("REQUEST_METHOD") == 'POST':
		items = db.getCartItems(autenticate)
		db.clearCart(autenticate)
		deliveryAddress = parser.parseData(sys.stdin.read())
		print("""\
			<div>
			<p> Your items will be delivered at:  
			""" + deliveryAddress['address'] + """\
			<br />List of items to be delivered: </p>
			</div>
		""")
	structure.printItemContents(items)
	