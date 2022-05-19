"""Given an array of integers of size ‘n’, Our aim is to calculate the maximum
sum of ‘k’ consecutive elements in the array.
Input  : arr[] = {100, 200, 300, 400}, k = 2
Output : 700
Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}, k = 4 
Output : 39
We get maximum sum by adding subarray {4, 2, 10, 23} of size 4.
Input  : arr[] = {2, 3}, k = 3
Output : Invalid
There is no subarray of size 3 as size of whole array is 2."""

# O(n*k)
def max_sum(arr, k):
    max_sum = float('-inf')
    for i in range(len(arr)-k+1):
        curr_sum = 0
        for j in range(k):
            curr_sum += arr[i+j]
        if max_sum < curr_sum:
            max_sum = curr_sum
    return max_sum

# O(n*k)
def max_sum1(arr, k):
    max_sum = float('-inf')
    for i in range(len(arr)-k+1):
        curr_sum = sum(arr[i:i+k])
        if max_sum < curr_sum:
            max_sum = curr_sum
    return max_sum


# sliding window with 2 variables tracking each sums and swap
def max_sum2(arr, k):
    max_sum = sum(arr[:k])
    curr_sum = max_sum
    for i in range(len(arr)-k):
        curr_sum = curr_sum - arr[i] + arr[i+k]
        if max_sum < curr_sum:
            max_sum = curr_sum
    return max_sum


arr = [1, 4, 2, 10, 2,
       3, 1, 0, 20]
k = 4

print(max_sum(arr,k))
print(max_sum1(arr,k))
print(max_sum2(arr,k))