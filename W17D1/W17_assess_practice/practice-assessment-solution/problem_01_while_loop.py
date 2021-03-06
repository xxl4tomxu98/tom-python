# WHILE LOOP
#
# In this problem, write a function named "my_while_loop" that accepts an
# iterable of strings as a parameter and returns a new list with strings from
# the original list that are longer than five characters. The function must use
# a while loop in its implementation.
#
# There are two sample data calls for you to use.

# WRITE YOUR FUNCTION HERE
def my_while_loop(lst):
    new_lst = []
    i = 0
    while i < len(lst):
        if len(lst[i]) > 5:
            new_lst.append(lst[i])
        i += 1
    return new_lst


# TEST DATA
test = ["nope", "yes this one", "not", "uhuh", "here's one", "narp"]
print(my_while_loop(test))  # > ["yes this one", "here's one"]

test = ["plop", "", "drop", "zop", "stop"]
print(my_while_loop(test))  # > []

test = []
print(my_while_loop(test))  # > []
