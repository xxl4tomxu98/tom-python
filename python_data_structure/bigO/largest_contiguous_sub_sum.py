'''Largest Contiguous Sub-sum
You have an array of integers and you want to find the largest contiguous (together in sequence)
sub-sum. Find the sums of all contiguous sub-arrays and return the max.

Example:

    list = [5, 3, -7]
    largest_contiguous_subsum(list) # => 8

    # possible sub-sums
    [5]           # => 5
    [5, 3]        # => 8 --> we want this one
    [5, 3, -7]    # => 1
    [3]           # => 3
    [3, -7]       # => -4
    [-7]          # => -7
Example 2:

    list = [2, 3, -6, 7, -6, 7]
    largest_contiguous_subsum(list) # => 8 (from [7, -6, 7])
Example 3:

    list = [-5, -1, -3]
    largest_contiguous_subsum(list) # => -1 (from [-1])'''

#this solution O(n3) in time and space
def largest_contiguous_subsum(list):
    if len(list)==0:
        return None
    if all(x < 0 for x in list):
        return max(list)
    all_sum_arrs = []
    for i in range(len(list)):
        for j in range(i, len(list)):
            all_sum_arrs.append(sum(list[i:j+1]))
    return max(all_sum_arrs)

print(largest_contiguous_subsum([5, 3, -7]))
print(largest_contiguous_subsum([2, 3, -6, 7, -6, 7]))
print(largest_contiguous_subsum([-5, -1, -3]))

# this solution is O(n) in time and O(1) in space
def largest_contiguous_subsum1(list):
    if len(list)==0:
        return None
    if all(x < 0 for x in list):
        # all negatives largest would be single element
        return max(list)
    #use one pointer largest for traversal, current for cum
    largest = list[0]
    current = largest
    for i in range(1,len(list)):
        # this is to eliminate negative because they don't contribute to larger num
        if current < 0:
            current = 0        
        current += list[i]
        if current > largest:
            largest = current
    return largest
    
print(largest_contiguous_subsum1([5, 3, -7]))
print(largest_contiguous_subsum1([2, 3, -6, 7, -6, 7]))
print(largest_contiguous_subsum1([-5, -1, -3]))