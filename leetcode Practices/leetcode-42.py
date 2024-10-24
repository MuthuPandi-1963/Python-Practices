def trap(height):
    # n=len(nums)
    # left=0
    # right=n-1
    # mid=0
    # store1=0
    # while(left < right and nums[left] < nums[left+1]): left+=1 
    # while(left < right and nums[right] < nums[right-1]): right-=1 
    # while(left < right):
    #     mid=left+1
    #     wall=mid
    #     while(mid < right and nums[left] > nums[mid]):
    #         if(nums[mid]>nums[wall]):
    #             wall=mid
    #         mid+=1
    #     if(nums[mid]>nums[wall]):
    #             wall=mid
    #     if(wall!=mid): mid=wall
    #     maxl=min(nums[left],nums[wall])
    #     while(left < mid):
    #         if(nums[left] < maxl):
    #             store1+=maxl-nums[left]
    #             left+=1
    #         else:
    #             left+=1
    # print(store1)
    n=len(height)
    left = 0
    right = n - 1
    maxLeft = 0
    maxRight = 0
    trappedWater = 0
    while (left <= right):
        if (height[left] <= height[right]):
            if (height[left] >= maxLeft):
                maxLeft = height[left]
            else:
                trappedWater += maxLeft - height[left]
            left+=1
        else:
            if (height[right] >= maxRight):
                maxRight = height[right]
            else:
                trappedWater += maxRight - height[right]
            right-=1
    print(trappedWater)
    return trappedWater




# trap([0,1,0,2,1,0,1,3,2,1,2,1])
# trap([4,2,0,3,2,5])
# trap([4,2,3])
# trap([9,6,8,8,5,6,3])
trap([2,6,3,8,2,7,2,5,0])
