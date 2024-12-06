# output

"""
                1
             2  4
          3  5  7
       6  8 10 12
    9 11 13 15 17
14 16 18 20 22 24
"""

n=6
odd=1
even = 2
for i in range(1,n+1):
    s=""
    for j in range(0,n-i):
        s+=" "
    for k in range(1,i+1):
        if i%2==1 :
            s+= str(odd)+""
            odd+=2
        else:
           s+=str(even)+""
           even+=2 
    print(s)