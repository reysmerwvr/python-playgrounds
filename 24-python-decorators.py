def hello():

    def welcome():
        return "hello"

    return welcome


print(hello())
#######################################################################################################################
list1 = [1, 2, 3]


def hello():
    number = 50

    def welcome():
        return "hello"

    #     print(locals())
    #     print(globals())
    return welcome


print(hello())

print(globals().keys())
print(globals()['list1'])
print(list1)


#######################################################################################################################

def hello():
    def welcome():
        return "hello"

    return welcome


print(hello()())

hello_func = hello()
hello_func()

del hello_func

hello()


#######################################################################################################################


def hello():
    return "Hello!"


def test(function):
    print(function())


test(hello)


#######################################################################################################################

def hello():
    print("Hello!")


def good_bye():
    print("Good Bye!")


def monitor(function):
    def decorator():
        print("\t Function will be executed: ", function.__name__)

        function()

        print("\t Function executed successfully: ", function.__name__)

    return decorator


monitor(hello)()
monitor(good_bye)()


#######################################################################################################################

@monitor
def hello():
    print("Hello!")


@monitor
def good_bye():
    print("Good Bye!")


hello()
good_bye()


#######################################################################################################################


def monitor_args(function):
    def decorator(*args, **kwargs):
        print("\t Function will be executed: ", function.__name__)

        function(*args, **kwargs)

        print("\t Function executed successfully: ", function.__name__)

    return decorator


@monitor_args
def hello(name):
    print("Hello {}!".format(name))


@monitor_args
def good_bye(name):
    print("Good Bye {}!".format(name))


hello("John")
good_bye("John")
