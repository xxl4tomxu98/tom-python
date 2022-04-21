"""Time Complexity Analysis: O(nlog(n))
n is the size of the input array
step-1 requires O(n) time as previously discussed
step-2's while loop requires n steps in isolation and each deleteMax will require
log(n) steps to restore max heap property (due to sifting-down). This means step 2
costs O(nlog(n)). The total time complexity of the algorithm is 
O(n + nlog(n)) = O(nlog(n)), space complexity is O(n) for heap array
"""
import math
from MaxHeap import MaxHeap

def heapSort(array):
    heap = MaxHeap()
    for ele in array:
        heap.insert(ele)
    
    sorted = []
    while len(heap.array) > 1:
        sorted.append(heap.deleteMax())
    return sorted


print(heapSort([21, 100, 22, 35, 42]))




def swap(array, i, j):
    [array[i], array[j]] = [array[j], array[i]]

# sift-down the node at index i until max heap property is restored
# n represents the size of the heap without initial None, i.e. num of nodes
def heapify(array, n, i):
    #Using these as our child index formulas will allow us to avoid using
    #a placeholder element at index 0. The root of the heap will be at index 0
    leftIdx = 2 * i + 1
    rightIdx = 2 * i + 2

    if leftIdx >= n:
        leftVal = -math.inf
    else:
        leftVal = array[leftIdx]
    if rightIdx >= n:
        rightVal = -math.inf
    else:
        rightVal = array[rightIdx]    

    if (array[i] > leftVal) & (array[i] > rightVal):
        return

    if leftVal < rightVal:
        swapIdx = rightIdx
    else:
        swapIdx = leftIdx
    
    swap(array, i, swapIdx)
    heapify(array, n, swapIdx)


def heapSortInPlace(array):
    #heapify the tree from the bottom up
    for i in range(len(array)-1, -1, -1):
        heapify(array, len(array), i)
    
    # the entire array is now a heap
    # until the heap is empty, continue to "delete max"
    for endOfHeap in range(len(array)-1, -1, -1):
        #swap the root of the heap with the last element of the heap,
        #this effecively shrinks the heap by one and grows the sorted array by one
        swap(array, endOfHeap, 0)

        #sift down the new root, but not past the end of the heap
        heapify(array, endOfHeap, 0)
    
    return array

print(heapSortInPlace([21, 100, 22, 35, 42]))
