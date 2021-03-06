#!/usr/bin/python3

import Helpers.db as db
import Helpers.myparser as parser
import Helpers.structure as structure
import Helpers.nav as nav
import Helpers.validator as validator
import os, sys

db.connectDB()
cookie = parser.parseCookie(os.getenv("HTTP_COOKIE"))
autenticate = db.checkSession(parser.parseCookie(os.getenv("HTTP_COOKIE"))) if validator.validateSession(cookie) else None
if autenticate == None :
	#print("Location: http://localhost/cgi-bin/MA-Shop/security_ec_shop/login.py")
	print("Location: https://172.24.129.8/login.py")
	print()
else :
	print("Content-Type: text/html\r\n\r\n")
	structure.printStartSection()
	nav.printNav(autenticate, db.cartCount(autenticate))
	form = """\
			<div>
			<form method="POST"> 
				<label for="address">Enter the addres to deliver your items: </label>
				<input id="address" name="address" maxlength="100" type="text" />
				<button>Submit</button>
			</form>
			
			<p> Your items to be delivered: </p>
			</div>
	 	"""
	if os.getenv("REQUEST_METHOD") == 'GET':
		print(form)
		items = db.getCartItems(autenticate)

	if os.getenv("REQUEST_METHOD") == 'POST':
		deliveryAddress = parser.parseData(sys.stdin.read())
		result = validator.validateAddress(deliveryAddress)
		if result == True : 
			items = db.getCartItems(autenticate)
			db.clearCart(autenticate)		
			print("""\
				<div>
				<p> Your items will be delivered at:  
				""" + deliveryAddress['address'] + """\
				<br />List of items to be delivered: </p>
				</div>
			""")
		else:	
			items = db.getCartItems(autenticate)			
			print("""<div>
				<p> The address should contain only letters, numbers, dots or commas, anything else, we think is suspicious</p>
				</div>""")
			print(form)
			
	structure.printItemContents(items, 0)
	
