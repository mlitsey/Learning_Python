import pymssql

connsql = pymssql.connect(server='localhost', user='sa', password='P@ssw0rd', database='AdventureWorks2017')
cursorsql = connsql.cursor()
#replace your for loop with parameterized executemany statement
cursorsql.execute("select * from person.person")
cursorsql.close()
connsql.close()