def maximumSubArray(nums:list):
    n=len(nums)
    for i in range(n):
        print(sum(nums[i:]) ,"    ",sum(nums[0:n-1-i]))
        
    
    # maximum=max(nums)
    # left=0
    # right=0
    # values=[sum(nums),maximum]
    # while(left<=right):
    #     if(maximum-nums[left]>maximum):
    #         values.append(maximum-nums[left])
    #         left+=1
    #     else:
    #         left+=1
    #     if(maximum-nums[right]>maximum):
    #         values.append(maximum-nums[right])
    #         right-=1
    #     else:
    #         right-=1
    # return (max(values))
print(maximumSubArray([-2,1,-3,4,-1,2,1,-5,4]))
# print(maximumSubArray([5,4,-1,7,8]))
# print(maximumSubArray([-1]))
# print(maximumSubArray([-2,1]))



