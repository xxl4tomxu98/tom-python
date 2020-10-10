Week 17 Review - Python Intro
Number Data Type
Explain the most common types of numbers in Python
int
float
complex
Evaluate arithmetic expressions that include familiar operators and **, // and %
Predict when an arithmetic expression will throw an error
String Data Type
Write strings using the correct syntax
Use len() to obtain a count of the number of characters in a string
Refer to one or more characters in a string
Concatenate strings together
Variables
Predict when errors will be thrown when using variables and expressions
Explain the meaning of None in Python
Boolean Data Type
Predict the evaluation of expressions that use the boolean operations of and, or and not
Explain how Python handles non-Boolean objects in conditional statements (Truthy and Falsey)
Know the various falsey values in Python
Comparison Operators
Understand that conditionals in Python return boolean values
Understand what the operators >,<, >=, <=, ==, and != do
Identity vs. Equality
Explain the difference between == and is
If Statements
Know how to write an if statement in Python, and what the elif and else blocks do.
While Statements
Understand the syntax for a Python while loop:
while condition:
  do_something()
Understand what break and continue do in the context of a while loop
Try/Except Statements
Write a try statement to catch and handle exceptions in Python
Handle different types of errors
pass
Understand what the Python pass statement is for, and when to use it
Functions
Describe how to define a function in Python

Create a named function with def
Create an anonymous function with lamda
Demonstrate how to invoke a function

Write functions which could do some/all of these:

Accepts parameters
Return a value
Return a function
Understand the use of *args and *kwargs in function definitions

When ordering arguments within a function or function call, arguments need to occur in a particular order:

Formal positional arguments
*args
Keyword arguments with default values
**kwargs
Know that Python keeps track of extra arguments and will provide them to your function using:

The parameter that starts with * will receive a tuple of values that are the extra positional parameters
The parameter that starts with ** will receive a dictionary of values that are the extra keyword parameters
Formatting Strings
Generate formatted output using join and format
Getting Input From The Command Line
Know how to use the input() function to get responses from a CLI user
Structured Data
Define sequence, collection and iterable

BONUS: Know which built-in classes are immutable and which are mutable.

Built-in Data Types
Be able to declare a list, tuple, range, dictionary and set in Python
Built-in Functions
Use functions with iterables filter, map, sorted, enumerate, zip
ex: Creating a list with filter extracting short strings from list lst:
lst = ["cat", "at", "a"]
list(filter(lambda el: len(el) < 3, lst))
# => returns ["at", "a"]
lambda el: len(el) < 3 is an anonymous function
filter passes each el from lst to the anonymous function
filter returns a generator function that will yield all els that evaluated to True in the lambda function
list() casts the result of the generator function as a list
ex: Creating a list with map squaring num from nums:
nums = [1, 2, 3]
set(map(lambda num: num ** 2, nums))
# => returns {1, 4, 9}
lambda num: len(num) < 3 is an anonymous function
map passes each num from nums to the anonymous function
map returns a generator function that will yield nums that have been squared from nums
set() casts the result of the generator function as a set
Analyze iterables using len, max, min, sum, any, all
Work with sets using operators &, |, -, ^
Use the predefined typecasting functions like int(), float(), str(), etc. to perform explicit type conversion.
for Statements
Understand the one-and-only syntax for a Python for loop:
for item in iterable:
  # do something with the item
  print(item)
Understand what break and continue do in the context of a for loop
Importing in Python
Define module in Python
Use import to load a built-in module
Follow common best practices for importing modules
Classes in Python
How to use the class keyword to define a class

How to name classes

How to create instances from classes

How to initialize classes with the dunder method __init__()

How to declare instance methods for a class

How to make string representations of classes using dunder methods

__str__() to generate a human-friendly string representing your class (<Dog: Fido>)
__repr__() to generate string equivalent of the python initializer call ("Dog(name='Fido')")
BONUS: How to use the dunder class variable __slots__ to reserve memory for instance variables

Inheritance in Python
Use parentheses after the class name to specify the parent class

Use the super() method to access methods on the parent class

BONUS: Python supports multiple inheritance, so more than one parent class can appear in the class declaration - these should be separated by commas.

Properties in Python
You create the getter property by decorating a method with @property.
You create the setter property by decorating a corresponding method with the decorator @<getter_method_name>.setter.
List Comprehensions
Know what a list comprehension is:
[<map> for <selector> in <iterator> if <filter>]
<iterator> provides values to the comprehension (required)
<selector> initializes the loop variable(s) (required)
<map> is an expression that may transform the loop variable(s) (required but could be trivial (ex: the first i in [i for i in lst]))
<filter> filters on the loop variable(s) (optional)
