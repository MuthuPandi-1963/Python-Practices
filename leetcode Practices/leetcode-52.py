def floorSortedArray(arr:list,x:int):
    n=len(arr)
    left=0
    right=n-1
    while(left<right):
        mid=(left+right)//2
        if(arr[mid]<x):
            left=mid+1
        elif (arr[mid]>x):
            right=mid-1
    print(left-1)
floorSortedArray([1,2,8,10,11,12,19],5)
floorSortedArray([1,2,8,10,11,12,19],0)