def searchInsert(nums, target):
        n=len(nums)
        left=0
        right=n-1
        while(left<=right):
            mid=(left+right)//2
            if nums[mid]==target:
                print(mid)
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        print(left)
        return left
searchInsert([1,3,5,6],5)
searchInsert([1,3,5,6],2)
searchInsert([1,3,5,6],7)
        