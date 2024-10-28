n=5

for i in range(n):
    s=""
    for j in range(n-1-i):
        s+=" "
    for k in range((2*i)+1):
        if k==0 or k==(2*i):
            s+="*"
        else:
            s+=" "
    print(s) 
for i in range(n-2,-1,-1):
    s=""
    for j in range(n-1-i):
        s+=" "
    for k in range((2*i)+1):
        if k==0 or k==(2*i):
            s+="*"
        else:
            s+=" "
    print(s) 