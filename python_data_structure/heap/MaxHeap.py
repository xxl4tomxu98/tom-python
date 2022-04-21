import math
class MaxHeap:
    def __init__(self):
        self.array = [None]
    
    def getParent(self, idx):
        return idx // 2
    
    def getLeftChild(self, idx):
        return idx * 2
    
    def getRightChild(self, idx):
        return idx * 2 + 1    

    def insert(self, val):
        self.array.append(val)
        self.siftUp(len(self.array) - 1)
        
    def siftUp(self, idx):
        if idx == 1:
            return        
        parentIdx = self.getParent(idx)
        if self.array[parentIdx] < self.array[idx]:
            [self.array[parentIdx], self.array[idx]] = [self.array[idx], self.array[parentIdx]]
            self.siftUp(parentIdx)      
    
    def deleteMax(self):
        if len(self.array) == 2:
            return self.array.pop()
        if len(self.array) == 1:
            return None

        max = self.array[1]
        self.array[1] = self.array.pop()
        self.siftDown(1)
        return max
    
    def siftDown(self, idx):
        ary = self.array        
        leftIdx = self.getLeftChild(idx)
        rightIdx = self.getRightChild(idx)

        if (leftIdx <= len(ary) -1):
            leftVal = ary[leftIdx]
        else:
            leftVal = -math.inf

        if (rightIdx <= len(ary) -1):
            rightVal = ary[rightIdx]
        else:
            rightVal = -math.inf
    
        if (ary[idx] > leftVal) & (ary[idx] > rightVal):
            return
    
        if leftVal < rightVal:
            swapIdx = rightIdx
        else:
            swapIdx = leftIdx        
    
        [ary[idx], ary[swapIdx]] = [ary[swapIdx], ary[idx]]
        self.siftDown(swapIdx)


heap = MaxHeap()
heap.insert(42)
heap.insert(35)
heap.insert(22)
heap.insert(100)
heap.insert(110)
heap.insert(21)

heap.deleteMax()


print(heap.array)