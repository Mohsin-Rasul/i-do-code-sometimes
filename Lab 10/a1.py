def linearSearch(arr, n, x):
    count = 0
    found = False
    
    for i in range(n):
        count = count + 1
        if arr[i] == x:
            found = True
            break
            
    if found == True:
        print("Student is Registered")
    else:
        print("Student is NOT Registered")
        
    print("Comparisons made:", count)


rolls = [1023, 1045, 1011, 1098, 1076, 1054, 1032]
target = 1076
n = len(rolls)

linearSearch(rolls, n, target)