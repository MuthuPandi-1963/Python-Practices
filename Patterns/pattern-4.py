# input n=5

# Output 
#  *********
#  *       *
#  *       *
#  *       *
#  *       *
#  *       *
#  *       *
#  *       *
#  *       *
#  *       *
#  *********
n=5
# for i in range(2*n+1):
#     s=" "
#     for j in range(2*n-1):
#         if i==0 or i==2*n:
#             s+="*"
#         elif (i>=1 and i<=2*n-1) and (j==0 or j==2*n-2):
#             s+="*"
#         elif j>=1 and j<=2*n-1:
#             s+=" "
#     print(s)

for i in range(n):
    s=""
    for j in range(n):
        if i==0 or i==n-1:
            s+="*"
        elif (i>=1 and i<=n-1) and (j==0 or j==n-1):
            s+="*"
        elif j>=1 and j<=n-2:
            s+=" "
    print(s)

     
for i in range(n):
    s="" 
    for j in range(n):
        if i==0 or i==n-1:
            s+="*"
        else:
            if j==0 or j==n-1:
                s+="*"
            else:
                s+=" "
    print(s)