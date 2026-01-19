def LS(arr,n,x):
    count=0
    found=False
    for i in range(n):
        count+=1
        if arr[i]==x:
            found=True
            break

    if found==True:
        print("Item Found")
    else:
        print("Not")
    print("Number of comparisons:",count)


arr=[2,3,4,10,40]
x=10
n=len(arr)
result=LS(arr,n,x)
