sum = 0
n=4
for i in range(1,n+1):
    s=" "
    sum+=i
    val=sum
    for j in range(n-i):
        s+="-"
    for k in range(i):
        s+=str(val)+" "
        val-=1
    print(s)
# sum = 0
for i in range(n-1,0,-1):
    s=" "
    # sum+=i
    val=sum
    for j in range(n-i):
        s+="-"
    for k in range(i):
        s+=str(val)+" "
        val-=1
    print(s)