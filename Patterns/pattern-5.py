n=5
s="ABCDE"
for i in range(n):
    o=" "
    for j in range(n-i):
        o+=s[j]
    print(o)