def binarySearch(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            low=mid-1

    return False
        
arr=[10,20,30,40,50,60,70,80,90]
target=70
result=binarySearch(arr,target)
if result is not False:
    print("Element found at index:",result)
else:
    print("Element not found")
