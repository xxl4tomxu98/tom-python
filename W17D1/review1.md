Python Day 3
More on Comprehensions
In Python, a comprehension is "a set of looping and filtering instructions". From the Python Language Reference, p73:

For constructing a list, a set or a dictionary Python provides special syntax called “displays”, each of them in two flavors:

• either the container contents are listed explicitly, or

• they are computed via a set of looping and filtering instructions, called a comprehension.

Comprehensions can be used anywhere a corresponding list, dictionary or set could be used.

old_list = range(20)

# a list comprehension
new_list = [i * 4 for i in old_list if i % 2]
# [4, 12, 20, 28, 36, 44, 52, 60, 68, 76]

# a set comprehension
{suit.title() for suit in ('hearts', 'spades', 'diamonds', 'clubs')}
# {'Diamonds', 'Spades', 'Hearts', 'Clubs'}

# a dictionary comprehension - map names to the number of vowels in them...
{name: len(list(filter(lambda letter: letter in 'aeiou',name.lower())))
  for name in ('gordon', 'DAVID', 'walter', 'josephina', 'Ariadne') }
# 'gordon': 2, 'DAVID': 2, 'walter': 2, 'josephina': 4, 'Ariadne': 4}
List comprehensions generate an ordered list of elements; set and dict comprehensions generate a list of keys and key:value pairs, respectively.

Placing the code that would create a list comprehension between parentheses rather than braces creates a generator which is a code construct that when iterated over yields the same values as would be present in the corresponding list, were it created. Because a generator does not need to be evaluated until it is called, there is no separate storage required for the returned values.

More on Slices
ranges and slices are related concepts in Python. From the Python Language Reference glossary:

slice - An object usually containing a portion of a sequence. A slice is created using the subscript notation, [] with colons between numbers when several are given, such as in variable_name[1:3:5]. The bracket (subscript) notation uses slice objects internally.

Slices are created whenever a sequence is indexed with an expression that has colons in it.

# copy a sequence entirely
copied = original[:]

# skip the first character
rest = original[1:]

# get everything but the last character
beginning = original[:-1]

# get every other character starting with the second one
odds = original[1::2]
Slicing creates a new sequence. The construct original[:] will often be used to create a (shallow!) copy of original.

lambda functions
In Python, a lambda function is an anonymous function; these are often used for purposes similar to what anonymous callback functions are used for in JavaScript. The syntax for a lambda function is lambda <parameters>: <returned_expression>:

print(list(map(lambda x: x ** 3, range(5)))) # [0, 1, 8, 27, 64]

# consider this definition
def cubed(n):
  return n ** 3

# and this one
cubed = lambda n: n ** 3

# these are equivalent expressions; both create a function called 'cubed' that
# takes a single value and returns the cube of it.  The second form is considered "not pythonic", and is discouraged, but the code generated is the same in both cases.
sorting
There are two common functions related to sequences of values that can re-order the values, sort and sorted. sort is a command to re-order a sequence in place; sorted takes a sequence and returns a new, sorted one. Both make use of an optional keyword, key. When this parameter (usually a function) is provided, it is evaluated for each element in the sequence, and the return value is used to determine the sorting order for the result.

# get some objects to sort
persons = Person.all()

# create a new list, sorted by SSN
sp_ssn = sorted(persons, key=lambda person: person.ssn)

# sort the person list in place by date of birth, reversed
persons.sort(key=lambda person: person.dob, reverse=True)
logging basics
Python has a rich collection of tools to support logging. The downside of this is that the documentation can be very difficult to parse without a way in. Here is all you need to know to start logging effectively in Python!

Logging in Python consists of connecting sources of debugging information - a Logger object - to a destinations for that information - Handler objects. The handler has a helper object, a Formatter, that determines how the information is formatted. A formatter is created with a printf dict-style formatting string and an optional separate formatter for timestamps. Both logger objects and handler objects have a filtering level associated with them - here are the logging Levels available, along with their numeric weights:

| Level | Value | | :--------- + ------: | | CRITICAL | 50 | | ERROR | 40 | | WARNING | 30 | | INFO | 20 | | DEBUG | 10 | | NOTSET | 0 |

A logger or handler object will only pass messages at the level it is set at or higher; for instance, a handler with a level of WARNING will pass WARNING, ERROR and CRITICAL messages, but will ignore DEBUG and INFO messages.

The various fields that can be added to a Formatter are described in the table in section 16.6.7 (LogRecord attributes) in the Python Library Reference.

At its simplest, logging in Python requires:

Importing the logging module
creating a Logger object, and setting its Level property
creating a Handler object, and setting its Level propery
creating a Formatter object, and binding it to the Handler
binding the Handler object to the Logger object
The example code below does all of these things, directing logging output to a simple StreamHandler which will log directly to the system console. (Many other Handler types are available - see section 16.8 of the Python Standard Library)

################################################################################
# configure logging - here we just log to the console
################################################################################

import logging

logger = logging.Logger(__file__)
# set the level for this logger
logger.setLevel(logging.DEBUG)

# set the level for the (console) logging handler
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)

# define a format string for logging output
formatter = logging.Formatter("%(asctime)s "
                              "(%(filename)s:%(funcName)s:%(lineno)d) "
                              "[%(levelname)s]: %(message)s")

# attach the formatter to the handler
handler.setFormatter(formatter)
# and the handler to the logger
logger.addHandler(handler)

################################################################################
Python Logging Documentation
The API reference information is located at section 16.6 of the Python Standard Library.
More narrative help is available in the Logging HOWTO and Logging Cookbook documents.
Formatting Strings - ALL the Options!
printf style formatting
In the previous set of notes (W17D2) we looked in some detail at the printf style string formatting available through the use of the % operator. ("%s, %s" % (last, first) or "%(last)s, %(first)s" % person.__dict__) Replacable expressions in the format string start with the % character and end with a type specifier. In between these can come width, justification, padding and precision specifiers, as well as dictionary keys in the second form. This approach to formatting strings is documented in section 4.7.2 in the Python Standard Library. It is the original approach - very powerful, and you will see it in older code - but it has fallen from favor as it is somewhat cryptic and error-prone, especially for new users.

str.format() style formatting
The str.format() method was introduced in Python 2.6, and there was some expectation that it would replace the older method - but this method has issues too. The str.format() approach is documented in section 6.1.2-3 of the Python Standard Library. Calling this method on a string with replacement parameters results in the replacement expression {...} with the corresponding parameter from the parameter list:

>>> "The sum of 1 + 2 is {0}".format(1+2)
'The sum of 1 + 2 is 3'
(The Format Specification Mini-Language is described starting on p100 of the Python Standard Library)

Section 6.1.4 of the Python Standard Library (Template strings) provides another take on format strings in Python.

The biggest problem with this approach (besides stubborn developers!) is that properly specified format strings get a lot longer, once all of the referenced names are embedded in them.

f-string formatting (aka Formatted string literals)
With the introduction of Python 3.6 a "new, new" method was introduced - f-strings. Described in PEP 498, and documented in section 2.4.3 of the Python Language Reference, this approach looks (to me) a lot like string interpolation in JavaScript. From the documentation:

A formatted string literal or f-string is a string literal that is prefixed with 'f' or 'F'. These strings may contain replacement fields, which are expressions delimited by curly braces {}. While other string literals always have a constant value, formatted strings are really expressions evaluated at run time. Like the backtick strings in JS, the {...} replacement expressions in f-strings can be arbitrarily complicated Python expressions, in addition to literals and variables. Formatting specifiers can be added, and have a syntax similar to the specifiers in printf style format strings:

>>> name = "Fred"
>>> f"He said his name is {name!r}."
"He said his name is 'Fred'."
>>> f"He said his name is {repr(name)}." # repr() is equivalent to !r
"He said his name is 'Fred'."
>>> width = 10
>>> precision = 4
>>> value = decimal.Decimal("12.34567")
>>> f"result: {value:{width}.{precision}}" # nested fields
'result: 12.35'
>>> today = datetime(year=2017, month=1, day=27)
>>> f"{today:%B %d, %Y}" # using date format specifier
'January 27, 2017'
>>> f"{today=:%B %d, %Y}" # using date format specifier and debugging
'today=January 27, 2017'
>>> number = 1024
>>> f"{number:#0x}" # using integer format specifier
'0x400'
>>> foo
>>> f"{
" foo =
>>> line = "The mill's closed"
>>> f"{line = }"
'line = "The mill\'s closed"'
>>> f"{line = :20}"
"line = The mill's closed "
>>> f"{line = !r:20}"
'line = "The mill\'s closed" '
(So many choices!)

Properties!
From the Built-in Functions section of the Python Library Reference:

class property(fget=None,fset=None,fdel=None,doc=None)

Return a property attribute.

fget is a function for getting an attribute value. fset is a function for setting an attribute value. fdel is a function for deleting an attribute value. And doc creates a docstring for the attribute.

A typical use is to define a managed attribute x:

class C:
  def __init__(self):
    self._x = None

  def getx(self):
    return self._x

  def setx(self, value):
    self._x = value

  def delx(self):
    del self._x

  x = property(getx, setx, delx, "I'm the 'x' property.")
If c is an instance of C, c.x will invoke the getter, c.x = value will invoke the setter and del c.x the deleter. If given, doc will be the docstring of the property attribute. Otherwise, the property will copy fget’s docstring (if it exists). This makes it possible to create read-only properties easily using property() as a decorator:

class Parrot:
  def __init__(self):
    self._voltage = 100000

  @property
  def voltage(self):
    """Get the current voltage."""
    return self._voltage
The @property decorator turns the voltage() method into a “getter” for a read-only attribute with the same name, and it sets the docstring for voltage to “Get the current voltage.” A property object has getter, setter, and deleter methods usable as decorators that create a copy of the property with the corresponding accessor function set to the decorated function. This is best explained with an example:

class C:
  def __init__(self):
    self._x = None

  @property
  def x(self):
    """I'm the 'x' property.""" return self._x

  @x.setter
  def x(self, value):
    self._x = value

  @x.deleter
  def x(self):
    del self._x
This code is exactly equivalent to the first example. Be sure to give the additional functions the same name as the original property (x in this case.) The returned property object also has the attributes fget, fset, and fdel corresponding to the constructor arguments. Changed in version 3.5: The docstrings of property objects are now writeable.

NOTE: "Be sure to give the additional functions the same name as the original property" - when the official documentation asserts something I have disagreed with, one of us is probably wrong. just sayin' :D
