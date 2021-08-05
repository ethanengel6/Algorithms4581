import random, time



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

print(mergeSort([1,1,1,6,8,3,2,1,7,0]))

def insertSort(L):
    for i in range (1,n):
        key = L[i]
        j=i-1
        while j>=0 and L[j]>key:
            L[j+1]=L[j]
            j=j-1
        L[j+1] = key
    return(L)


def bubbleSort(L):
    for q in range(len(L)):
        for z in range(len(L)-1):
            if L[z]>L[z+1]:
                L.insert(z+1,L.pop(z))
    return(L)

print("N\t\tMerge\t\tInsert\t\tBubble")
for n in range(100,5100,100):
    A = [i for i in range(n)]
    random.shuffle(A)
    t1 = time.time()
    B = mergeSort(A)
    t2 = time.time()
    mtime = round((t2-t1)*1000,1)
    random.shuffle(A)
    t3 = time.time()
    C = insertSort(A)
    t4=time.time()
    itime=round((t4-t3)*1000,1)
    random.shuffle(A)
    t5=time.time()
    D=bubbleSort(A)
    t6=time.time()
    btime=round((t6-t5)*1000,1)
    print(n,"\t\t",mtime,"\t\t",itime,"\t\t",btime)
