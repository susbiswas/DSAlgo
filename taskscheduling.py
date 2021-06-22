def taskscheduling(A):
    n = len(A)
    L = []
    L.append(A[0])
   

    for i in range(1,n):
       t = L[len(L)-1]
       #if (last task inserted endtime < currently visited task start time) and
       # (last task inserted starttime > currently visited task start time)
       if (t[1] < A[i][0]) and (A[i][0] > t[0]):
           L.append(A[i])
            

    print(L)
    return len(L)
L=[]
L.append([1, 4])
L.append([3, 5])
L.append([0, 6])
L.append([5, 7])
L.append([3, 8])
L.append([5, 9])
L.append([6, 10])
L.append([8, 11])
L.append([8, 12])
L.append([2,13])
L.append([12, 14])

print(taskscheduling(L))








