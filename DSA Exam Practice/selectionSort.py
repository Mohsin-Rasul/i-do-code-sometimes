def selectionSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            minIndex=i
            if arr[j]<arr[minIndex]:
                minIndex=j
        if minIndex!=i:
            arr[i],arr[minIndex]=arr[minIndex],arr[i]
    return arr

arr=[64,25,12,22,11]
sortedArr=selectionSort(arr)
print("Sorted array is:",sortedArr)
