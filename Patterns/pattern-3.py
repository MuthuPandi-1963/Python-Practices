# input n=5

""" output: 

    12345
    12345
    12345
    12345
    12345
"""

n=5

#method -1
for i in range(n):
    star =""
    for j in range(n):
        star+=str(j+1)
    print(star)


print("    ")

#method -2 
x="12345"
for i in range(n):
    print(x)
   
