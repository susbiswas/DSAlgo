def isMaxHeap(A,i):
    n = len(A)

    l_child = 2*i+1
    r_child = 2*i+2

    if l_child > n-1:
        return True
    
    elif r_child > n-1:
        if A[i] > A[l_child]:
            return True
        else:
            return False
    if A[i] > A[l_child] and A[i] > A[r_child]:
        if isMaxHeap(A,l_child) and isMaxHeap(A,r_child):
            return True
        else:
            return False
    else:
        return False

print(isMaxHeap([100,19,36,17,3,25,10,2,7],0))

print(isMaxHeap([90,89,70,36,75,63,71,21,18,77],0))

    