# WHILE LOOP
#
# In this problem, write a function named "my_while_loop" that accepts an
# iterable of strings as a parameter and returns a new list with strings from
# the original list that are longer than five characters. The function must use
# a while loop in its implementation. The order of the strings in the new list
# must be in the same order they were in the old list.
#
# There are two sample data calls for you to use.

# WRITE YOUR FUNCTION HERE
def my_while_loop(strings):
  results = []
  index = 0
  while index < len(strings):
    if len(strings[index])>5:
      results.append(strings[index])
    index += 1
  return results

# TEST DATA
test = ["nope", "yes this one", "not", "uhuh", "here's one", "narp"]
print(my_while_loop(test))  # > ["yes this one", "here's one"]

test = ["plop", "", "drop", "zop", "stop"]
print(my_while_loop(test))  # > []

test = []
print(my_while_loop(test))  # > []
