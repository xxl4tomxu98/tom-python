import math
from MaxHeap import MaxHeap
# you may assume that the array will always have a null element at the 0-th index
def isMaxHeap(array, idx=1):
    if idx > len(array)-1:
        return True
    leftIndex = idx * 2
    rightIndex = idx * 2 + 1
    if leftIndex > len(array)-1:
        leftVal = -math.inf
    else:
        leftVal = array[leftIndex]
    if rightIndex > len(array)-1:
        rightVal = -math.inf
    else:
        rightVal = array[rightIndex]
    
    return (array[idx] > leftVal) & (array[idx] > rightVal) \
           & isMaxHeap(array, leftIndex) & isMaxHeap(array, rightIndex)

print(isMaxHeap([None, 100, 42, 22, 35, 21]))
print(isMaxHeap([None, 21, 100, 22, 35, 42]))