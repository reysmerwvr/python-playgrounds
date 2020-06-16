import local_modules.module_docstrings as module_docstrings


def hello(arg):
    """This is the docstring of the hello function"""
    print("Hello", arg, "!")


hello("John")
help(hello)


class Class:
    """This is the docstring of the class Class"""

    def __init__(self):
        """This is the docstring of init method of Class"""
        pass

    def method(self):
        """This is the docstring of a method of Class"""
        pass


cls = Class()

help(cls)

module_docstrings.hello()
module_docstrings.good_bye()

help(module_docstrings)
print(dir(module_docstrings))
print(module_docstrings.__name__)
print(module_docstrings.__package__)
print(module_docstrings.__doc__)

help(print)
help(len)

# pydoc -w module_name
# pydoc -w package_name
# pydoc -w package_name .\
# pydoc -b
# pydoc -p 8000

# epydoc http://epydoc.sourceforge.net/
# sphinx https://www.sphinx-doc.org/en/master/
