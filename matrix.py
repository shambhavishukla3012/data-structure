def matrix(Rows, Columns):
    mat =[]
    for row in range(Rows):
        a =[]
        for col in range(Columns): 
            a.append(int(input()))
        mat.append(a)
    # return mat
    for row in range(Rows):
        for col in range(Columns): 
            print(mat[row][col], end=' ')
        print()
        
    print(mat)
    print(mat[0])
    print(mat[0][0])
    
matrix(2,2)
# print(b)