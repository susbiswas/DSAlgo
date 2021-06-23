def binarysearch(A,low,high,x):
    if high >= low:
        mid = (high+low)//2

        if A[mid]== x:
            return mid
        elif A[mid]>x:
            return binarysearch(A,low,mid-1,x)
        else:
            return binarysearch(A,mid+1,high,x)

        
    else:
        return -1
A = [10,-3,15,100,35,28,90,11,5,7]
print(binarysearch(A,0,len(A),15))
