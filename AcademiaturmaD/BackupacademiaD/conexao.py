import mysql.connector
banco=mysql.connector.connect(host="localhost",user="root",password="0120",database="academiaturmad")
print(banco)

meucursor=banco.cursor()