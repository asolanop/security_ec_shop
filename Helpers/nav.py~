#!/usr/bin/python3

def printNav(autenticate, item_count = None):
	if autenticate == None :
		print("""
		<ul>
		<li><a href="index.py">Home</a></li>
		<li><a href="register.py">Register</a></li>
		<li><a href="login.py">Login</a></li>
		<li><a href="feedback.py">Contact</a></li>
		</ul>""") 
	else :
		print("""
		\
		<ul>
		<li><a href="index.py">Home</a></li>
		<li><a href="addItem.py">New Product</a></li>
		<li><a href="checkout.py">My Cart""")
		
		if item_count != None :
			print(" (" + str(item_count) + ") ")
		
		print("""</a></li>
		<li><a href="feedback.py">Contact</a></li>		
		<li><a href="logout.py">Logout</a></li>
		</ul>
		""") 
