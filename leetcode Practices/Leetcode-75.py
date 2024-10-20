
"""
75. Sort Colors
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
"""

def SortColors(nums):
    n=len(nums)
    zeros,ones,twos=0,0,0
    for i in range(n):
        if(nums[i]==0):
            zeros+=1
        elif nums[i]==1:
            ones+=1
        else:
            twos+=1
        
        # for i in range(n):
        # nums[zeros+ones-1]=1
    while( n > zeros+ones):
        n-=1
        nums[n]=2
        
    while(n >  zeros):
        n-=1
        nums[n]=1
    while(n>0):
        n-=1
        nums[n]=0
        

    print(nums)
# nums = [2,0,2,1,1,0]
# SortColors(nums)
SortColors([2, 1, 0, 1, 2, 1, 0, 1, 2, 0])
SortColors([1, 2, 1, 2, 0])
nums=[1, 2, 0, 1, 2, 0, 1, 2]
SortColors(nums)
