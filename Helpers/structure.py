#!/usr/local/bin/python3

def printStartSection():
	print("<html>")
	print("""<head><link rel="stylesheet" href="http://localhost/css/style.css">
		<title> El Mercadito Musical </title> </head>""")
	print("<body>")
	print("""<div id="principaldiv"><img id="principalhome" src="http://localhost/css/header.png"></div>""")

def printSearchForm():
	print (""" <div id="searchdiv">
		<form method="GET" action="search.py">
			<label for="search">Search by: </label>
			<input id="search" name="search" maxlength="50" />
 			<button id="submit" type="submit">Submit</button><br>
		<br />
		</form>
	</div>""")

def printItemContents(items, addPosibility):
	#action="http://localhost/cgi-bin/MA-Shop/security_ec_shop/search.py"

	bigtempl = '''<center>
        		<table border="0" cellspacing="15">
        			{rows}
        		</table>
    		</center>'''

	#action="http://localhost/cgi-bin/MA-Shop/security_ec_shop/addToCart.py">
	rowtempl = ""
	if addPosibility == 1:
		rowtempl = """
		<tr>
		    <td align="center">
		    <p class="sansserif"> 
			<b> {name} </b> <br>
			Description: {descrip} <br>
			Price: {price}
			</p>
			<form method="POST" action="addToCart.py">
			<input type="hidden" name="itemID" value={id} />
			<button type="submit">Add to Cart</button><br>
			</form>
		    </td>
		</tr>
		"""
	else: 
		rowtempl = """
		<tr>
		    <td align="center">
		    <p class="sansserif"> 
			<b> {name} </b> <br>
			Description: {descrip} <br>
			Price: {price}
			</p>
			<form method="POST" action="addToCart.py">
			<input type="hidden" name="itemID" value={id} />
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
