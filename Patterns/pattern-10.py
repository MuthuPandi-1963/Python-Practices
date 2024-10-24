#input n=5
"""
output
    1 2 3 4 5
    2 3 4 5 1
    3 4 5 1 2 
    4 5 1 2 3
    5 1 2 3 4
"""
n=5
for i in range(n):
    s=""
    for j in range(1,n+1):
        if (j+i >=6):
            s+=str(j+i-n)+" "
        else:
            s+=str(j+i)+" "
    print(s)