# input n=5

""" output: 

    *  
    **
    ***
    ****
    *****
"""

n=5

#method -1
for i in range(n):
    star =""
    for j in range(i+1):
        star+="*"
    print(star)
print("    ")

#method -2
for i in range(n):
    print("*"*(i+1))
   
