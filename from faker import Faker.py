from faker import Faker
f = Faker()

import sqlite3

connection = sqlite3.connect('database_faker.db')

cursor = connection.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS user (UserId INTEGER PRIMARY KEY NOT NULL, FirstName VARCHAR(20), LastName VARCHAR(20), Birthday DATE , Email VARCHAR(20), Address INTEGER FOREIGN KEY Address REFERENCE address(AdressId) )')
cursor.execute('CREATE TABLE IF NOT EXISTS address (UserId INTEGER FOREIGN KEY REFERENCES user(UserId), Address VARCHAR(50), Country VARCHAR(30), City VARCHAR(50), PostalCode VARCHAR(10), PhoneNumber VARCHAR(20))')
cursor.execute('CREATE TABLE IF NOT EXISTS product (Name VARCHAR(15), Inventory INTEGER, Price INTEGER)')
cursor.execute('CREATE TABLE IF NOT EXISTS cart (UserId INTEGER NOT NULL, ProductId  INTEGER NOT NULL, Quantity INTEGER)')
cursor.execute('CREATE TABLE IF NOT EXISTS command (UserId  INTEGER NOT NULL, ProductId  INTEGER NOT NULL, Quantity INTEGER)')
cursor.execute('CREATE TABLE IF NOT EXISTS invoices (BillingAddress VARCHAR(80), BillingCity VARCHAR(20), BillingCountry VARCHAR(20), BillingPostalCode VARCHAR(20),Total INTEGER)')

# UserId INTEGER NOT NULL / PROBLEM AVEC LA CONTRAINTE UNIQUE



# cursor.execute('DROP TABLE user')
# cursor.execute('DROP TABLE address')
# cursor.execute('DROP TABLE product')
# cursor.execute('DROP TABLE cart')
# cursor.execute('DROP TABLE command')
# cursor.execute('DROP TABLE invoices')

#cursor.execute('DELETE FROM user')

number = 20
i = 1
# id = cursor.id
# print('id: %d' % id)

#USER
for i in range(number):
      cursor.execute('INSERT INTO user VALUES (:UserId,:FirstName, :LastName, :Birthday, :Email)',
                  {'UserId': int(i+1),'FirstName': f.first_name(), 'LastName': f.last_name(), 'Birthday': f.date(), 'Email': f.email()}
    )

# #ADDRESS
# for y in range(number):
#     cursor.execute('INSERT INTO address VALUES (:Address, :Country, :City, :PostalCode, :PhoneNumber )',
#         {'Address':f.address() ,'Country': f.country(), 'City': f.city(), 'PostalCode': f.postcode(), 'PhoneNumber': f.phone_number()}
#     )

#INVOICES
# for k in range(number):
#     cursor.execute('INSERT INTO invoices VALUES (:BillingAddress, :BillingCity, :BillingCountry, :BillingPostalCode, :Total)',
#         {'BillingAddress': f.address(), 'BillingCity': f.city(), 'BillingCountry': f.country(), 'BillingPostalCode': f.postcode(), 'Total': int()}
#     ) 

#PRODUCT
# for v in range(number): 
#     cursor.execute('INSERT INTO product VALUES (:Name, :Inventory, :Price)',
#     {'Name': f.name(), 'Inventory': f.pyint(5), 'Price': int(2)}
#     )

#COMMAND
# for w in range(number): 
#     cursor.execute('INSERT INTO command VALUES (:Id, :UserId, :ProductID, :Quantity)',
#     {'Id':f.pyint(1,20), 'UserID': f.pyint(1,20), 'ProductId': f.pyint(1,20), 'Quantity': int(1,10)}
#     )

#CART
# for a in range(number): 
#     cursor.execute('INSERT INTO cart VALUES (:Id, :UserId, :ProductId, :Quantity)',
#     {'Id':f.pyint(1,20), 'UserId': f.pyint(1,20), 'ProductId': f.pyint(1,20), 'Quantity': int(1,10)}
#     )


connection.commit()

connection.close()