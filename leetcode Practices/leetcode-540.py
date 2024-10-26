def singleNonDuplicate(nums) -> int:
    n=len(nums)
    if n==1:
        return nums[0]
    left=0
    right=n-1
    while(left<=right):
        mid=(left+right)//2
        if mid%2==0:
            if mid<n-1:
                if nums[mid] ==nums[mid+1]:
                    left=mid+1
                elif nums[mid]==nums[mid-1]:
                    right=mid-1
                else:
                    return nums[mid]
            else:
                return nums[mid]
        else:
            if mid<n-1:
                if nums[mid-1] ==nums[mid]:
                    left=mid+1
                elif nums[mid]==nums[mid+1]:
                    right=mid-1
                else:
                    return nums[mid]
            else:
                return nums[mid]
print(singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
print(singleNonDuplicate([3,3,7,7,10,11,11]))
print(singleNonDuplicate([1]))
print(singleNonDuplicate([1,1,2,2,3]))
print(singleNonDuplicate([1,1,2,3,3]))
