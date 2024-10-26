def setZeros(matrix:list):
    n=len(matrix)
    m=len(matrix[0])
    row=[0]*n
    col=[0]*m
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                col[j]=1
                row[i]=1
    print(row,col)
    for i in range(n):
        if row[i]==1:
            for j in range(m):
                matrix[i][j]=0
    for i in range(m):
        if col[i]==1:
            for j in range(n):
                matrix[j][i]=0
    print(matrix)



setZeros([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
setZeros([[1,1,1],[1,0,1],[1,1,1]])