import pymssql  
conn = pymssql.connect(server='localhost', user='sa', password='P@ssw0rd', database='AdventureWorks')  
cursor = conn.cursor()  
cursor.execute('SELECT c.CustomerID, c.CompanyName SalesLT.Customer;')  
row = cursor.fetchone()  
while row:  
    print (row[0] + " " + row[1] + " " + row[2])     
    row = cursor.fetchone()  