#!/usr/bin/python3

import Helpers.db

def printHeaders():
	print("Content-Type: text/html\r\n\r\n")

def printStartSection():
	print("<html>")
	print("<head><title> El Mercadito Musical </title> </head>")
	
def printHomeBody():
	Helpers.db.init()
	print("<body>")
	print("<h2>El Mercadito Musical</h2>")
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
	items = Helpers.db.getAllItems()
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
	#Helpers.db.connectDB()
	print("</body>")



def printEndSection():
	print("</html>")

printHeaders()
printStartSection()
printHomeBody()
printEndSection()
