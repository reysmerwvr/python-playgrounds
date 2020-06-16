# class Vehicle:
#     def __init__(self, color, wheels):
#         self.color = color
#         self.wheels = wheels
#     def __str__(self):
#         return "color {}, {} wheels".format(self.color, self.wheels)
#
# class Car(Vehicle):
#     def __init__(self, color, wheels, speed, displacement):
#         self.color = color
#         self.wheels = wheels
#         self.speed = speed
#         self.displacement = displacement
#     def __str__(self):
#         return "color {}, {} km/h, {} wheels, {} cc".format(self.color, self.speed, self.wheels, self.displacement)
#
#
# c = Car("blue", 150, 4, 1200)
# print(c)

# class Vehicle:
#     def __init__(self, color, wheels):
#         self.color = color
#         self.wheels = wheels
#     def __str__(self):
#         return "color {}, {} wheels".format(self.color, self.wheels)
#
# class Car(Vehicle):
#     def __init__(self, color, wheels, speed, displacement):
#         Vehicle.__init__(self, color, wheels)
#         self.speed = speed
#         self.displacement = displacement
#     def __str__(self):
#         return Vehicle.__str__(self) + ", {} km/h, {} cc".format(self.speed, self.displacement)  # using super()
#
# c = Car("blue", 4, 150, 1200)
# print(c)
#
# class Vehicle:
#     def __init__(self, color, wheels):
#         self.color = color
#         self.wheels = wheels
#     def __str__(self):
#         return "color {}, {} wheels".format(self.color, self.wheels)
#
# class Car(Vehicle):
#     def __init__(self, color, wheels, speed, displacement):
#         super().__init__(color, wheels)  # using super() without self instead of Vehicle
#         self.speed = speed
#         self.displacement = displacement
#     def __str__(self):
#         return super().__str__() + ", {} km/h, {} cc".format(self.speed, self.displacement)
# c = Car("blue", 4, 150, 1200)
# print(c)


class Vehicle:

    def __init__(self, color, wheels):
        self.color = color
        self.wheels = wheels

    def __str__(self):
        return "color {}, {} wheels".format(self.color, self.wheels)


class Car(Vehicle):

    def __init__(self, color, wheels, speed, displacement):
        super().__init__(color, wheels)  # using super() without self instead of Vehicle
        self.speed = speed
        self.displacement = displacement

    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.speed, self.displacement)


class Van(Car):
    def __init__(self, color, wheels, speed, displacement, load):
        super().__init__(color, wheels, speed, displacement)
        self.load = load

    def __str__(self):
        return super().__str__() + ", {} lbs of load".format(self.load)


class Bicycle(Vehicle):
    def __init__(self, color, wheels, model):
        super().__init__(color, wheels)
        self.model = model

    def __str__(self):
        return super().__str__() + ", {}".format(self.model)


class Motorcycle(Bicycle):
    def __init__(self, color, wheels, model, speed, displacement):
        super().__init__(color, wheels, model)
        self.speed = speed
        self.displacement = displacement

    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.speed, self.displacement)


vehicles = [
    Car("blue", 4, 150, 1200),
    Van("white", 4, 100, 1300, 1500),
    Bicycle("green", 2, "btx"),
    Motorcycle("black", 2, "ducatti", 180, 900)
]


# def classify(vehicle_list):
#     for vehicle in vehicle_list:
#         print("{} {}".format(type(vehicle).__name__, vehicle))

# classify(vehicles)

def classify(vehicle_list, wheels=None):
    """
    :param wheels:
    :type vehicle_list: object
    """
    for vehicle in vehicle_list:
        if wheels is None:
            print("{} {}".format(type(vehicle).__name__, vehicle))
        elif vehicle.wheels == wheels:
            print("{} {}".format(type(vehicle).__name__, vehicle))


classify(vehicles, 2)
