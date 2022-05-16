'''Execution Time Difference
Learning Goals
Be able to determine the time and space complexity of a method
Be able to compare the time complexity of one method to another
Be able to recognize when time or space complexity can be improved
my_min
Given a list of integers find the smallest number in the list.

Example
    list = [ 0, 3, 5, 4, -5, 10, 1, 90 ]
    my_min(list)  # =>  -5
'''
#this is O(n) time and O(1) space
def my_min(list):
    min = list[0]
    # traversal the list using min to track lower values
    for i in list[1:]:
        if min > i:
            min=i
    return min

print(my_min([ 0, 3, 5, 4, -5, 10, 1, 90 ]))