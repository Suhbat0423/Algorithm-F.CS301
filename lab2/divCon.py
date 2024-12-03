def findMax(arr, low, high):
    if low == high:
        return arr[low]

    mid = (low + high) // 2

    left_max = findMax(arr, low, mid)
    right_max = findMax(arr, mid + 1, high)

    return max(left_max, right_max)

arr = [1, 5, 3, 9, 2, 8]
result = findMax(arr, 0, len(arr) - 1)
print(result)  
