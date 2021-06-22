class compositeElement:
  def __init__(self, key, pos):
    self.key = key
    self.pos = pos

# algorithm for merging two lists 
def merge(A,B):
  C = []
  while len(A)>0 and len(B)>0:
    if A[0].key < B[0].key:
      x = A.pop(0)
      C.append(x)
    else:
      x = B.pop(0)  
      C.append(x)
  if len(A)>0:
    C.extend(A)   # append list A to the end of list C
  else:
    C.extend(B)
  return C        # running time O(len(A)+len(B)) 

#  merge sort: what an elegant function!
def mergeSort(L):
  n = len(L)
  if n==1:
    return L
  else:
    A = mergeSort(L[0:(n//2)])
    B = mergeSort(L[(n//2):n])
    C = merge(A,B)
    return C      # running time O(nlog n): huge savings over selection sort!

def updatedMergeSort(I):
  n = len(I)
  L=[]
  for i in range (0,n):
    L.append(compositeElement(key = I[i], pos = i+1))
  
  L = mergeSort(L)
  n = len(L)
  key = []
  pos = []
  for i in range(0,n):
    key.append(L[i].key)
    pos.append(L[i].pos)

  print(key)
  print(pos)

A = [10, 3, 5]
updatedMergeSort(A)

  
