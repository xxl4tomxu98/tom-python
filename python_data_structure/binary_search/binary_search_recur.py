def binarySearch(array, target):
    if len(array) == 0:
        return False
    
    midIdx = len(array) // 2
    leftHalf = array[0 : midIdx]
    rightHalf = array[midIdx + 1 :]

    if target < array[midIdx]:
        return binarySearch(leftHalf, target)
    elif target > array[midIdx]:
        return binarySearch(rightHalf, target)
    else:
        return True
   

print(binarySearch([5, 10, 12, 15, 20, 30, 70], 12))
print(binarySearch([5, 10, 12, 15, 20, 30, 70], 24))