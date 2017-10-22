#!/usr/bin/python3

def printNav(autenticate):
	if autenticate == None :
		print("""
		<ul>
		<li><a href="http://localhost/cgi-bin/MA-Shop/security_ec_shop/index.py">Home</a></li>
		<li><a href="http://localhost/cgi-bin/MA-Shop/security_ec_shop/register.py">Register</a></li>
		<li><a href="http://localhost/cgi-bin/MA-Shop/security_ec_shop/login.py">Login</a></li>
		</ul>""") 
	else :
		print("""
		<ul>
		<li><a href="http://localhost/cgi-bin/MA-Shop/security_ec_shop/index.py">Home</a></li>
		<li><a href="http://localhost/cgi-bin/MA-Shop/security_ec_shop/addItem.py">New Product</a></li>
		<li><a href="http://localhost/cgi-bin/MA-Shop/security_ec_shop/index.py">My Cart</a></li>
		<li><a href="http://localhost/cgi-bin/MA-Shop/security_ec_shop/logout.py">Logout</a></li>
		</ul>""") 
