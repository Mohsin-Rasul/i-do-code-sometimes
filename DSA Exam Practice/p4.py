
def mergeSort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=mergeSort(arr[:mid])
    right=mergeSort(arr[mid:])

    return merge(left,right)


def merge(left,right):
    sortedList=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            sortedList.append(left[i])
            i+=1
        else:
            sortedList.append(right[j])
            j+=1
    sortedList.extend(left[i:])
    sortedList.extend(right[j:])

    return sortedList

arr=[38,27,43,3,9,82,10]
sortedArr=mergeSort(arr)
print("Sorted array:",sortedArr)
