def getlandpoints(filename):
    # Using readlines()
    file1 = open(filename, 'r')
    Lines = file1.readlines()
    indexList = []

    count = 0
    i = 0
    for line in Lines:
        if count > 2 and count < 11:
            i+=1
            charArray = list(line)
            for j in range (0,len(charArray)):
                if charArray[j] == 'X':
                    indexList.append([i,j])
        count+=1

    return indexList
indexList = getlandpoints('/Users/susmitabiswas/MSCS/Summer2021/CS610/Programs/Python/Susmita-Biswas.txt')
print(indexList)

def coordinatetonumber(i,j,m,n):
    if i< m and j <n:
        return (i*m)+(j)
    else:
        print("Invalid index")

print(coordinatetonumber(6,5,10,10))

def numbertocoordinate(t,m,n):
    if t < m*n:
        return [(t//m),(t%n)]
    else:
        print("Invalid index")

print(numbertocoordinate(52,10,10))

import math
def distance(t1,t2):
    co_ord1 = numbertocoordinate(t1,10,10)
    co_ord2 = numbertocoordinate(t2,10,10)

    if co_ord1[0] == co_ord2[0]:    #if both are in same row
        distance = co_ord1[1]-co_ord2[1] if co_ord1[1]>co_ord2[1] else co_ord2[1]-co_ord1[1]
        distance = distance - 1
    else:
      distance = performcalculation(co_ord1,co_ord2) if co_ord1[0]>co_ord2[0] else performcalculation(co_ord2,co_ord1)

    return distance

def performcalculation(pt1, pt2):
  row = (pt1[0]-pt2[0])-1
  column = pt1[1]-pt2[1] if pt1[1]>pt2[1] else pt2[1]-pt1[1]
  return row+column

print(distance(58,83))


