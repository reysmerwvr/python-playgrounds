import sqlite3

connexion = sqlite3.connect("example.db")

pointer = connexion.cursor()

pointer.execute("CREATE TABLE IF NOT EXISTS users (name VARCHAR(100), age INTEGER, email VARCHAR(100))")

# pointer.execute("INSERT INTO users  VALUES ('John Doe', 28, 'john@test.com')")

# pointer.execute("SELECT * FROM users")
# user = pointer.fetchone()
# print(user)

# users = [
#     ('Paul Doe', 28, 'paul@test.com'),
#     ('Mary Doe', 28, 'mary@test.com'),
# ]
#
# pointer.executemany("INSERT INTO users  VALUES (?, ?, ?)", users)

pointer.execute("SELECT * FROM users")
users = pointer.fetchall()
print(users)

for user in users:
    print(user[0], user[1], user[2])

connexion.commit()

connexion.close()
