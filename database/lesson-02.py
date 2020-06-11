import sqlite3

connexion = sqlite3.connect("users.db")

pointer = connexion.cursor()

# pointer.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#         dni VARCHAR(9) PRIMARY KEY,
#         name VARCHAR(100),
#         age Integer,
#         email VARCHAR(100)
#     )
#     ''')

# users = [
#     ('11111111A', 'Paul Doe', 28, 'paul@test.com'),
#     ('11111111B', 'Mary Doe', 28, 'mary@test.com'),
#     ('11111111C', 'George Doe', 28, 'george@test.com'),
# ]
#
# pointer.executemany("INSERT INTO users  VALUES (?, ?, ?, ?)", users)

# pointer.execute("SELECT * FROM users WHERE age=28")
#
# users = pointer.fetchall()
# print(users)

# pointer.execute("UPDATE users SET name='Josh Doe', age=29 WHERE dni='11111111A'")
pointer.execute("DELETE FROM users WHERE dni='11111111A'")

########################################################################################################################


# connexion = sqlite3.connect("products.db")
#
# pointer = connexion.cursor()
#
# pointer.execute('''
#     CREATE TABLE IF NOT EXISTS products (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name VARCHAR(100) NOT NULL,
#         brand VARCHAR(50) NOT NULL,
#         price FLOAT NOT NULL
#     )
#     ''')

# products = [
#     ('Keyboard', 'Apple', 20.00),
#     ('Monitor 20 inches', 'LG', 80.00),
# ]
#
# pointer.executemany("INSERT INTO products  VALUES (null, ?, ?, ?)", products)
#
# pointer.execute("SELECT * FROM products")
# products = pointer.fetchall()
# print(products)
#
# for product in products:
#     print(product)

connexion.commit()

connexion.close()
