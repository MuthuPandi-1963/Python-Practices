n=4

for i in range(2*n-1):
    s=""
    for j in range(2*n-1):
        top = i
        bottom = j
        right = (2*n - 2) - j
        left = (2*n - 2) - i
        s+=str(n- min(min(top,bottom) , min(left,right)))
    print(s)
        