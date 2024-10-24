n=5
for i in range(2*n+1):
    s=" "
    for j in range(2*n-1):
        if i==0 or i==10:
            s+="*"
        elif (i>=1 and i<=9) and (j==0 or j==8):
            s+="*"
        elif j>=1 and j<=7:
            s+=" "
    print(s)
     