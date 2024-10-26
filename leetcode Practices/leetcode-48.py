def rotateImage(matrix:list):
    n=len(matrix)
    m=len(matrix[0])
    arr=[]
    for i in range(m):
        s=[]
        for j in range(n):
            s.append(matrix[m-1-j][i])
        arr.append(s)
    for i in range(n):
        for j in range(m):
            matrix[i][j]=arr[i][j]
    print(arr)
    print(matrix)

rotateImage([[1,2,3],[4,5,6],[7,8,9]])
rotateImage([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])