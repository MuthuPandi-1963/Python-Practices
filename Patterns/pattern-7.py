n=5
count=0
for i in range(n):
    s=" "
    for j in range(i+1):
        count+=1
        s+=str(count)
    print(s)