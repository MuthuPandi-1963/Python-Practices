def nextPermutation(nums:list):
    n=len(nums)
    leader=False
    index=None
    for i in range(n-1,0,-1):
        if nums[i]>nums[i-1]:
            leader=True
            index=i-1
            break
    if(not leader):
        nums.reverse()
        return nums
    else:
        val=nums[index]
        for i in range(n-1,index,-1):
            if val<nums[i]:
                temp=nums[index]
                nums[index]=nums[i]
                nums[i]=temp
                break
        nums[index+1::]=sorted(nums[index+1::])
        return (nums)

        

print(nextPermutation([1,2,3]))
print(nextPermutation([3,2,1]))
print(nextPermutation([1,3,2]))
print(nextPermutation([2,3,1]))
print(nextPermutation([1,1,5]))
print(nextPermutation([1,2,3,4,5]))
print(nextPermutation([2,3,0,0,0,0,0]))