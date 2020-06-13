import sqlite3


def create_db():
    connexion = sqlite3.connect("restaurant.db")
    pointer = connexion.cursor()
    try:
        pointer.execute('''CREATE TABLE IF NOT EXISTS category(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(100) UNIQUE NOT NULL)
        ''')
        pointer.execute('''CREATE TABLE IF NOT EXISTS dish(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(100) UNIQUE NOT NULL, 
                    category_id INTEGER NOT NULL,
                    FOREIGN KEY(category_id) REFERENCES category(id))
            ''')
    except sqlite3.OperationalError:
        print("Tables already exist")
    else:
        print("Tables created successfully")
    finally:
        connexion.close()


def add_category():
    category_name = input("Type a new category...\n ")
    connexion = sqlite3.connect("restaurant.db")
    pointer = connexion.cursor()
    try:
        pointer.execute("INSERT INTO category VALUES (NULL, '{}')".format(category_name))
    except sqlite3.IntegrityError:
        print("The category {} already exist.".format(category_name))
    else:
        print("The category {} created successfully.".format(category_name))
    finally:
        connexion.commit()
        connexion.close()


def add_dish():
    connexion = sqlite3.connect("restaurant.db")
    pointer = connexion.cursor()
    categories = pointer.execute("SELECT * FROM category").fetchall()
    print("Select a category to add to the dish:")
    for category in categories:
        print("[{}] {}".format(category[0], category[1]))

    category_user = int(input("> "))

    dish = input("Name of the new dish? \n> ")

    try:
        pointer.execute("INSERT INTO dish VALUES (NULL, '{}', {})".format(dish, category_user))
    except sqlite3.IntegrityError:
        print("The dish {} already exist.".format(dish))
    else:
        print("The dish {} created successfully.".format(dish))
    finally:
        connexion.commit()
        connexion.close()


def show_menu():
    connexion = sqlite3.connect("restaurant.db")
    pointer = connexion.cursor()
    categories = pointer.execute("SELECT * FROM category").fetchall()
    for category in categories:
        print(category[1])
        dishes = pointer.execute("SELECT * FROM dish WHERE category_id={}".format(category[0])).fetchall()
        for dish in dishes:
            print("\t{}".format(dish[1]))
    connexion.close()


# Create database
create_db()

# Menu Options
while True:
    print("Welcome to my restaurant manager!")
    option = input("\nType an option: \n[1] Add new category\n[2] Add new dish\n[3] Show Menu\n[4] Quit\n\n")

    if option == "1":
        add_category()
    elif option == "2":
        add_dish()
    elif option == "3":
        show_menu()
    elif option == "4":
        print("Good Bye!")
        break
    else:
        print("Wrong option!")
