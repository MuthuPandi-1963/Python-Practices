# input n=5

""" output: 

    *****   
    *****
    *****
    *****
    *****
"""

n=5

#method -1
for i in range(n):
    star =""
    for j in range(n):
        star+="*"
    print(star)
   
print("    ")

#method -2
for i in range(n):
    print("*"*n)
   
