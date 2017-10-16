#!/usr/bin/python3

def printStartSection():
	print("<html>")
	print("<head><title> El Mercadito Musical </title> </head>")
	print("<body>")
	print("<h2>El Mercadito Musical</h2>")

def printItemContents(items):
	print (""" <div>
	<h2>Search:</h2>
		<form method="GET" action="../search.py">
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

	rowtempl = """
	<tr>
	    <td align="center" style="font-size:1.25em;">
	    <p class="sansserif"> <b> Name: {name} </b> <br>
	    Description: {descrip} </p>
	    </td>
	</tr>
	"""

	names_list = list()
	prices_list = list()
	descrip_list = list()	
	for row in items:
		names_list.append(row[0])
		prices_list.append(row[1])
		descrip_list.append(row[2])

	lst = zip(names_list, descrip_list)

	rows = [rowtempl.format(name=names_list, descrip=descrip_list) for names_list, descrip_list in lst]
	rows = "".join(rows)

	wholepage = bigtempl.format(rows=rows)
	print (wholepage)

# End body
def printEndSection():
	print("</body>")
	print("</html>")
