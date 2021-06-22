class myMinHeap:
    def __init__(self):
        self.H = []
        
    def insertMin(self,node):
        n = len(self.H)
        self.H.append(node)   # append in last leaf (next available position in array/list)

        if n == 0:
            self.H[0]=node
            return
    
        # now bubble up x
        pos = n;      # current position of bubble-up
        while pos>0:
            parent_pos = (pos-1)//2 
            if self.H[parent_pos].key > self.H[pos].key:  
                self.H[pos] = self.H[parent_pos]     # copy parent value to current position
                self.H[parent_pos] = node              # move x to parent's position
                pos = parent_pos                     # update current position
            else:
                break                                # break the bubble-up loop
    

    def heapMinRemove(self):
        x = self.H.pop()                   # pop last element
        self.H[0] = x                      # put it in the place of max 
        n = len(self.H)                    #calculate the length
        # now bubble-down x
        pos = 0
        while True:
            c1_pos = 2*pos+1            # child 1 position
            c2_pos = 2*pos+2            # child 2 position
    
            if c1_pos > n-1: # corrected the code by checking if left child doesn't exist
                break                          #then break the loop
            l_value = self.H[c1_pos].key

            if c2_pos > n-1: 
                r_value = l_value
            else:
                r_value = self.H[c2_pos].key

            if l_value <= r_value:
                c_pos = c1_pos
            else:
                c_pos = c2_pos            # which child is active in possible swap
            if self.H[pos].key> self.H[c_pos].key:
                self.H[pos] = self.H[c_pos]         # swap 
                self.H[c_pos] = x 
                pos = c_pos               # update current position
            else:
                break                     # break 