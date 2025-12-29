def binarySearch(arr, x, low, high):
    found = False
    
    print("Mid values:")
    
    while low <= high:
        mid = low + (high - low) // 2
        print(arr[mid])
        
        if arr[mid] == x:
            found = True
            break
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
            
    if found == True:
        print("Book is Available")
    else:
        print("Book is NOT Available")


books = [101, 115, 123, 130, 145, 150, 165, 178, 190]
target = 145
n = len(books)

binarySearch(books, target, 0, n - 1)