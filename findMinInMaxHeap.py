def findMinInMaxHeap(H):
    n = len(H)
    minValue = H[n//2]

    for i in range ((n//2)+1, n):
        minValue = min(minValue,H[i])
    print(minValue)

H = [100,19,25,4,8,-3]
findMinInMaxHeap(H)