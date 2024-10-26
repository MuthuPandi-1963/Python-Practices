def arrangeBySign(nums:int):
    n=len(nums)
    pos=0
    neg=1
    pointer=0
    arr=[0]*n
    while(pointer < n):
        if(nums[pointer]<0 and neg<n):
            arr[neg]=nums[pointer]
            neg+=2
        elif (nums[pointer]>=0 and pos<n):
            arr[pos]=nums[pointer]
            pos+=2
        pointer+=1
    for i in range(n):
        nums[i]=arr[i]
    print(nums)
arrangeBySign([-2,0,9,-1,3,5,-2,-3])
arrangeBySign([-2,0,9,-1,3,5,2,3])
arrangeBySign([28,-41,22,-8,-37,46,35,-9,18,-6,19,-26,-37,-10,-9,15,14,31])

print([28,-41,22,-8,46,-37,35,-9,18,-6,19,-26,15,-37,14,-10,31,-9])
print([28,-41,22,-8,-37,46,35,-9,18,-6,19,-26,-37,-10,-9,15,14,31])