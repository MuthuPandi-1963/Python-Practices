def searchRange(nums, target: int):
    n=len(nums)
    left=0
    right=n-1
    while(left<=right):
        mid=(left+right)//2
        if nums[mid]==target:
            min=mid
            max1=mid
            while(mid<=right):
                if nums[mid]==target:
                    max1=mid
                mid+=1
            mid=min
            while(mid>=left):
                if nums[mid]==target:
                    min=mid
                mid-=1
            return [min,max1]
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return [-1,-1]
print(searchRange([1],1))
print(searchRange([5,7,7,8,8,10],8))
print(searchRange([5,7,7,8,8,10],6))
print(searchRange([],0))
print(searchRange([2,2],2))
print(searchRange([3,3,3],3))
