
def linear(arr, x):
    count = 0
    for i in arr:
        count = count + 1
        if i == x:
            return count
    return count


def binary(arr, x):
    low = 0
    high = len(arr) - 1
    count = 0
    
    while low <= high:
        count = count + 1
        mid = low + (high - low) // 2
        
        if arr[mid] == x:
            return count
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return count


list1 = [402, 215, 678, 123, 890, 456]
list2 = [123, 215, 402, 456, 678, 890]
target = 456

c1 = linear(list1, target)
c2 = binary(list2, target)

print("Searching for:", target)
print("Linear comparisons:", c1)
print("Binary comparisons:", c2)