'''find_missing_number
Assume an array of non-negative integers. A second array is formed by shuffling the elements
of the first array and deleting a random element. Given these two arrays, find which element
is missing in the second array. Do this in linear time with constant memory use.

Method Signature
find_missing_number(array arr1, array arr2)

Example input/output
> find_missing_number([8,3,5,1], [1,5,3]) // = 8
> find_missing_number([1,1,1,1], [1,1,1]) // = 1
> find_missing_number([3,5,4,8,7,9], [7,4,3,5,9]) // = 8
'''

#Simpler than you think! Find the sums of the arrays and subtract the array with an item missing
# - the result should be the missing item. Time complexity: O(n) Space O(1), this is better than
# hash table method where new memory has to be acquired to create a hash table.
def find_missing_number(list1, list2):
    return sum(list1) - sum(list2)

print(find_missing_number([8,3,5,1], [1,5,3]))
print(find_missing_number([1,1,1,1], [1,1,1]))
print(find_missing_number([3,5,4,8,7,9], [7,4,3,5,9]))