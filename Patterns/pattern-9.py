n=5
for i in range(n):
    s=" "
    for j in range(1,n+1):
        if (j+i>=6):
            s+=str(j+i-n)
        else:
            s+=str(j+i)
    print(s)