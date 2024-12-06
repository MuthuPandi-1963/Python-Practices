# input n = 5
# output 

"""
     1
    21
   321
  4321
 54321
"""
n=5

for i in range(n,0,-1):
    s=""
    for j in range(i):
        s+=" "
    for k in range(n+1-i,0,-1):
        s+=str(k)
    print(s)