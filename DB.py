import mysql.connector

connection = mysql.connector.connect(host='127.0.0.1',
                                         database='mydb',
                                         user='julia',
                                         password='julia')
cursor = cursor = connection.cursor()

result = cursor.execute(""" SELECT product_id FROM product""")
print(result)
