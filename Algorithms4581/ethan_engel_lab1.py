

def printMatrix(m):
    for row in m:
        print(row)

def matrixMult(A, B):
    if len(A[0])!=len(B):
        print("Error: Number of columns for matrix A must = number of rows of matrix B")
        return None
    C = [[None for i in range(len(B[0]))] for j in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            sum=0
            for k in range(len(A[0])):
                sum=sum+A[i][k]*B[k][j]
            C[i][j]= sum
    return C



# Testing code
# Test1
A = [[ 2, -3, 3],
[-2, 6, 5],
[ 4, 7, 8]]
B = [[-1, 9, 1],
[ 0, 6, 5],
[ 3, 4, 7]]
C = matrixMult(A, B)
if not C == None:
    printMatrix(C)

# Test2
A = [[ 2, -3, 3, 0],
[-2, 6, 5, 1],
[ 4, 7, 8, 2]]
B = [[-1, 9, 1],
[ 0, 6, 5],
[ 3, 4, 7]]
C = matrixMult(A, B)
if not C == None:
    printMatrix(C)

# Test3
A = [[ 2, -3, 98, 5],
[-2, 6, 5, -2]]
B = [[-1, 9, 1],
[ 0, 6, 5],
[ 3, 4, 7],
[ 1, 2, 3]]
C = matrixMult(A, B)
if not C == None:
    printMatrix(C)
