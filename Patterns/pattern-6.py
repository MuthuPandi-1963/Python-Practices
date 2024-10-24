n=5
for i in range(n):
    s=" "
    for j in range(i+1):
        s+="*"
    print(s)
n=5
for i in range(1,n):
    s=" "
    for j in range(n-i):
        s+="*"
    print(s)     