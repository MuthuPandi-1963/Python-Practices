def CountSubArray(nums,k):
    n=len(nums)
    left=0
    mid=0
    count=0
    while(left < n):
        mid=left
        sum=0
        while(mid<n):
            sum+=nums[mid]
            if(sum==k):
                count+=1
            mid+=1
        left+=1
        

    print(count)

    
# CountSubArray([-1,-1,1],0)
# CountSubArray([1,-1,0],0)
# CountSubArray([-1,-2,-3],-3)
# CountSubArray([2,2,3,4,1,3,5,4],4)
# CountSubArray([1,1,1],2)
CountSubArray([1,2,3],3)
CountSubArray([2,2,4,4,2,1,1,4,3,1,2,2],4)
CountSubArray([3,1,2,1,1,2],4)