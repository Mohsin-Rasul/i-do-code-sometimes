def binaryS(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1

arr=[5,10,15,20,25,30,35,40,45,50]
target=25
result=binaryS(arr,target)
if result != -1:
    print("Element found at index:",result)
else:
    print("Element not found")