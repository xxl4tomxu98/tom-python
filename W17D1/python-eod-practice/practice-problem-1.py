# MAP
#
# In this problem, write a function named "lower_map" that accepts an
# iterable of strings as a parameter and returns a new list with strings from
# the original list that are all transformed to lower case. The function must
# use the map function.
#
# The str object in Python has a method on it named "lower".
#
# There are two sample data calls for you to use.

# WRITE YOUR FUNCTION HERE

def lower_map(lst):
  return list(map(lambda x: x.lower(), lst))

# TEST DATA
test = ["PLOP", "", "DROP", "ZOP", "STOP"]
print(lower_map(test))  # > ["plop", "", "drop", "zop", "stop"]

test = []
print(lower_map(test))  # > []
