'''Given an array of integers nums and an integer target, return indices of the two 
numbers such that they add up to target. You may assume that each input would have
exactly one solution. You may not use the same element twice.'''

from typing import List

# O(n2) brute force
def sumOfTwoNums(arr: List[int], target: int) -> (int, int):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return (i,j)
    

print(sumOfTwoNums([12, 34, 35, 201, -2, -102, 0, 4], -98))


# O(n)time and O(n) space solution Hash Table where numbers are keys and indexes are values
def twoSum(nums: List[int], target: int) -> List[int]:
    hash_map = {}
    for i in range(len(nums)):
        if nums[i] in hash_map:
            return [i, hash_map[nums[i]]]
        else:
            hash_map[target - nums[i]] = i


print(twoSum([12, 34, 35, 201, -2, -102, 0, 4], -98))