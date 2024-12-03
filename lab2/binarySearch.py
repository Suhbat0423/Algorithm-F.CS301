def binarySearch(arr, target, low, high):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binarySearch(arr, target, low, mid - 1)
        else:
            return binarySearch(arr, target, mid + 1, high)
    return -1

arr = [2, 3, 4, 10, 40]
target = 10
result = binarySearch(arr, target, 0, len(arr) - 1)
print(result)  
