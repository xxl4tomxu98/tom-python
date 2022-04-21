from MaxHeap import MaxHeap

def findKthLargest(nums, k):
    heap = MaxHeap()
    for num in nums:
        heap.insert(num)
    for i in range(1, k):
        heap.deleteMax()
    return heap.deleteMax()

print(findKthLargest([21, 100, 22, 35, 42], 3))