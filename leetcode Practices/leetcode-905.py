nums=[3,1,2,4]
t=nums.copy()
res=[]
for i in nums:
    if i %2==0:
        res.append(i)
        t.remove(i)
res.extend(t)
print(res)

