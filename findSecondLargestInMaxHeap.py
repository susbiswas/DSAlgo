def findSecondLargestInMaxHeap(A):
    pos = 0
    n = len(A)
    if n == 1:
        return A[0]
    elif n == 2:
        return A[1]
    else:
        l_child = 2*pos+1
        r_child = 2*pos+2

        if A[l_child] >= A[r_child]:
            return A[l_child]

        else:
            return A[r_child]

print(findSecondLargestInMaxHeap([100,19,36,17,3,25,10,2,7]))


print(findSecondLargestInMaxHeap([90,89,70,36,75,63,71,21,18,77]))