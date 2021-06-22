def delete(A,item):
    length = len(A)

    for i in range(0,length):
      if (A[i] == item):
        print("Item deleted",item)
        A.remove(A[i])
        break
        
    print("Item in A")
    for i in range(0,len(A)):
        print(A[i])
    return A
    
A = [1,6,-3,9,10,7,19,100]
A = delete(A,100)
A  = delete(A,-3)
A  = delete(A,1)