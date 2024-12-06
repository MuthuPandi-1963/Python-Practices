n=5
for i in range(n):
    s=""
    for j in range(i+1):
        if((i+j)%2==0):
            s+="1"
        elif ((i+j)%2==1):
            s+="0"
    print(s)    
