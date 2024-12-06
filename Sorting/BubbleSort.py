def BubbleSort(nums):
    n=len(nums)
    for i in range(n):
        for j in range(n-1-i):
            if(nums[j] > nums[j+1]):
                nums[j],nums[j+1] =nums[j+1],nums[j]
    print(nums)
            
            

value=[5,9,7,6,2,4,3,1,8,0]
BubbleSort(value)