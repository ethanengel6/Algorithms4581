def cPairDist(points):
    sorted=mergeSort(points)
    return(recCPairDist(sorted))

def mergeSort(L):
    if len(L) < 2:
        return L[:]
    else:
        mid = len(L)//2
        Left = mergeSort(L[:mid])
        Right = mergeSort(L[mid:])
        return merge(Left, Right)

def merge(A, B):
    out = []
    i,j = 0,0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            out.append(A[i])
            i += 1
        else:
            out.append(B[j])
            j += 1
    while i < len(A):
        out.append(A[i])
        i += 1
    while j < len(B):
        out.append(B[j])
        j += 1
    return out

def recCPairDist(points):
    n=len(points)
    if n<=3:
        return brute_force(points)
    mid = n // 2
    Q = points[:mid]
    R = points[mid:]

    dist1 = recCPairDist(Q)
    dist2 = recCPairDist(R)

    if dist1 <= dist2:
        d = dist1
    else:
        d = dist2

    d2= closest_split_pair(Q, R)

    if d <= d2:
        return d
    else:
        return d2

def brute_force(points):
    mi = abs(points[0]-points[1])
    p1 = points[0]
    p2 = points[1]
    ln_x = len(points)
    if ln_x == 2:
        return mi
    for i in range(ln_x-1):
        for j in range(i + 1, ln_x):
            if i != 0 and j != 1:
                d = abs(points[i]-points[j])
                if d < mi:
                    mi = d
                    p1, p2 = points[i], points[j]
    return mi

def closest_split_pair(first, last):
    dist = abs(first[-1]-last[0])
    return(dist)

print(cPairDist([7, 4, 12, 14, 2, 10, 16, 6]))
print(cPairDist([7, 4, 12, 14, 2, 10, 16, 5]))
print(cPairDist([14, 8, 2, 6, 3, 10, 12]))
