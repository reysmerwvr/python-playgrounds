from io import open
import pickle


class Character:

    # Constructor
    def __init__(self, name, life, attack, defense, scope):
        self.name = name
        self.life = life
        self.attack = attack
        self.defense = defense
        self.scope = scope

    def __str__(self):
        return '{} => {} life, {} attack, {} defense, {} scope'.format(self.name, self.life, self.attack, self.defense,
                                                                       self.scope)


class Handler:
    characters = []

    # Constructor
    def __init__(self, characters=[]):
        self.load()

    def add(self, character):
        for character_temp in self.characters:
            if character_temp.name == character.name:
                return
        self.characters.append(character)
        self.save()

    def destroy(self, name):
        for character_temp in self.characters:
            if character_temp.name == name:
                self.characters.remove(character_temp)
                self.save()
                print("\n Character {} deleted successfully".format(name))

    def show(self):
        if len(self.characters) <= 0:
            print("Empty Handler")
            return
        for character in self.characters:
            print(character)

    def load(self):
        try:
            file = open('characters.pickle', 'ab+')
            file.seek(0)
            self.characters = pickle.load(file)
        except Exception as inst:
            print(type(inst))  # the exception instance
            print(inst.args)  # arguments stored in .args
            print(inst)
        finally:
            file.close()
            print("It has been loaded {} characters".format(len(self.characters)))

    def save(self):
        try:
            file = open('characters.pickle', 'wb')
            pickle.dump(self.characters, file)
        except Exception as inst:
            print(type(inst))  # the exception instance
            print(inst.args)  # arguments stored in .args
            print(inst)
        finally:
            file.close()

    def __del__(self):
        # self.save()  # Automatically Save
        print("The file has been saved")


handler = Handler()
handler.add(Character("Gentleman", 4, 4, 4, 2))
handler.add(Character("Warrior", 2, 4, 2, 4))
handler.add(Character("Archer", 4, 3, 4, 8))
handler.show()

