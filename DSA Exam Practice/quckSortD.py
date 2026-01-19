def quickSort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[len(arr)//2]
    left=[x for x in arr if x<pivot]
    right=[x for x in arr if x>pivot]
    return quickSort(left)+[pivot]+quickSort(right)

arr=[3,6,8,10,1,2,1]
sortedArr=quickSort(arr)
print("Sorted array:",sortedArr)