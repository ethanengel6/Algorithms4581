
def printMatrix(m):
    for row in m:
        print(row)

def chainMatrix(dims):
# Create the empty 2-D table
    n = len(dims)-1
    m = [[None for i in range(n)] for j in range(n)]
    trace=[[None for i in range(n+1)] for j in range(n+1)]

# Fill in the base case values
    for i in range(n):
        m[i][i] = 0


    for chainLength in range(2,n+1):
        for i in range(n+1-chainLength):
            j = i + chainLength - 1

            m[i][j] = float("inf")
            for k in range(i,j):

                q = m[i][k]+m[k+1][j]+dims[i]*dims[k+1]*dims[j+1]
                if q < m[i][j]:
                    m[i][j] = q
                    trace[i+1][j+1]=k+1
    printMatrix(m)
    print(parenStr(trace,1,n))
    return m[0][n-1]


def parenStr(traceback,first,last):
    if first == last:
        print('A{}'.format(first-1), end='')
        return
    tr = traceback[first][last]
    print('(', end='')
    parenStr(traceback, first, tr)
    parenStr(traceback, tr + 1, last)
    print(')', end='')

dims = [30,35,15,5,10,20,25]
print(chainMatrix(dims))
