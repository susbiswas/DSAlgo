def ramanujan(n):
    tuple_dict = {}
    for i in range(1,n):
        for j in range (1,n):
            sum = i**3 + j**3
            if sum in tuple_dict:
                pair = tuple_dict.get(sum)
                for items in pair:
                    if i + j + items[0] + items[1] == n:
                        print(i ,j , items[0] ,items[1])

            else:
                tuple_dict[sum] = []

            tuple_dict[sum].append([i,j])

ramanujan(20)  