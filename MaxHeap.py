# The following code implements a **max** Heap
#
# Strictly speaking, the following functions will take O(n) time
# in Python, because changing an input array within the body of a function
# causes the language to copy the entire array. We will soon see how to do this 
# better, using Python classes


# function for inserting element in heap
def heapInsert(H,x):
  
  H.append(x)   # append in last leaf (next available position in array/list)
  n = len(H)

  
  # now bubble up x
  pos = n-1;      # current position of bubble-up
  while True:
    parent_pos = (pos-1)//2 
    if parent_pos<0:
      break
    if H[parent_pos] < H[pos]:  
      H[pos] = H[parent_pos]     # copy parent value to current position
      H[parent_pos] = x          # move x to parent's position
      pos = parent_pos           # update current position
    else:
      break                      # break the bubble-up loop
  return H

# function for removing max element from heap
# WARNING: This function is intentionally incomplete --
#          You will fix this in the assignment 

def heapMaxRemove(H):
  x = H.pop()                   # pop last element
  H[0] = x                      # put it in the place of max 
  n = len(H)                    #calculate the length
  # now bubble-down x
  pos = 0
  while True:
    c1_pos = 2*pos+1            # child 1 position
    c2_pos = 2*pos+2            # child 2 position
    
    if c1_pos > n-1: # corrected the code by checking if left or right child doesn't exist
      break                          #then break the loop
    l_value = H[c1_pos]
    if c2_pos > n-1:
      r_value = l_value
    else:
      r_value = H[c2_pos]

    if l_value >= r_value:
      c_pos = c1_pos
    else:
      c_pos = c2_pos            # which child is active in possible swap
    if H[pos]< H[c_pos]:
      H[pos] = H[c_pos]         # swap 
      H[c_pos] = x 
      pos = c_pos               # update current position
    else:
      break                     # break 

H=[]
H = heapInsert(H,25)
H = heapInsert(H,40)
H = heapInsert(H,-8)
print("Before delete")
print(H)

heapMaxRemove(H)
print("After delete")
print(H)