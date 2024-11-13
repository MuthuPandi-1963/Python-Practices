# nums=[-1,0,3,5,9,12]
# target=0
# index=-1
# for i in range(len(nums)):
#     if nums[i]==target:
#         index=i
#         break
# print(index)   


def binary_search(nums,target):
    n=len(nums)
    left=0
    right=n-1
    while(left<=right):
        mid=(left+right)//2
        if(target==nums[mid]):
            return(mid)
        elif(nums[mid]<target):
            left=mid+1
        else:
            right=mid-1
    return(-1)
print(binary_search([-1,0,3,5,9,12,15],2))
