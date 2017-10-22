#!/usr/bin/python3

def printStartSection():
	print("<html>")
	print("""<head><link rel="stylesheet" href="style.css">
		<title> El Mercadito Musical </title> </head>""")
	print("<body>")
	print("<h2>El Mecadito Birrero</h2>")
	#print('<img src="http://imgur.com/a/4XL4F" width="300" height="250">')

def printItemContents(items):
	#action="http://localhost/cgi-bin/MA-Shop/security_ec_shop/search.py"
	print (""" <div id="searchdiv">
		<form method="GET" action="http://localhost/search.py">
			<label for="search">Search by: </label>
			<input id="search" name="search" maxlength="50" />
 			<button type="submit">Submit</button><br>
		<br />
		</form>
	</div>""")

	bigtempl = '''<center>
        		<table border="0" cellspacing="15">
        			{rows}
        		</table>
    		</center>'''

	#action="http://localhost/cgi-bin/MA-Shop/security_ec_shop/addToCart.py">
	rowtempl = """
	<tr>
	    <td align="center">
	    <p class="sansserif"> 
		<b> {name} </b> <br>
		Description: {descrip} <br>
		Price: {price}
		</p>
		<form method="POST" action="http://localhost/addToCart.py">
		<input type="hidden" name="itemID" value={id} />
		<button type="submit">Add to Cart</button><br>
		</form>
	    </td>
	</tr>
	"""

	names_list = list()
	prices_list = list()
	descrip_list = list()
	id_list = list()
	for row in items:
		names_list.append(row[0])
		prices_list.append(row[1])
		descrip_list.append(row[2])
		id_list.append(row[3])
		
	lst = zip(names_list, prices_list, descrip_list, id_list)

	rows = [rowtempl.format(name=names_list, price=prices_list, descrip=descrip_list, id=id_list) 
		for names_list, prices_list, descrip_list, id_list in lst]
	rows = "".join(rows)

	wholepage = bigtempl.format(rows=rows)
	print (wholepage)

# End body
def printEndSection():
	print("</body>")
	print("</html>")
