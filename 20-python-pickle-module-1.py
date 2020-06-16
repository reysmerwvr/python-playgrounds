from io import open
import pickle


class Movie:

    # Constructor
    def __init__(self, title, time, year):
        self.title = title
        self.time = time
        self.year = year
        print('New movie has been created:', self.title)

    def __str__(self):
        return '{} ({})'.format(self.title, self.year)


class Catalogue:
    movies = []

    # Constructor
    def __init__(self, movies=[]):
        self.movies = movies
        self.load()

    def add(self, movie):
        self.movies.append(movie)
        self.save()

    def show(self):
        if len(self.movies) <= 0:
            print("Empty Catalogue")
            return
        for movie in self.movies:
            print(movie)

    def load(self):
        file = open('catalogue.pickle', 'ab+')
        file.seek(0)
        try:
            self.movies = pickle.load(file)
        except Exception as inst:
            print(type(inst))  # the exception instance
            print(inst.args)  # arguments stored in .args
            print(inst)
            print("Empty file")
        finally:
            file.close()
            del file
            print("It has been loaded {} movies".format(len(self.movies)))

    def save(self):
        file = open('catalogue.pickle', 'wb')
        pickle.dump(self.movies, file)
        file.close()
        del file

    def __del__(self):
        self.save()  # Automatically Save
        print("The file has been saved")


catalogue = Catalogue()
catalogue.show()
catalogue.add(Movie("The Godfather", 175, 1972))
catalogue.add(Movie("The Godfather II", 202, 1974))
catalogue.show()
del catalogue

catalogue = Catalogue()
catalogue.show()
catalogue.add(Movie("Toy Story", 202, 1999))
catalogue.show()
del catalogue

catalogue = Catalogue()
catalogue.show()
del catalogue
