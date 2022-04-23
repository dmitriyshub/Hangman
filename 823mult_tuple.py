

def mult_tuple(tuple1, tuple2):
    list_of_tuples = []
    for i in tuple1:
        for j in tuple2:

            list_of_tuples.append((i,j))
            list_of_tuples.append((j,i))

    return list_of_tuples


print(mult_tuple([1,2,3],[4,5,6]))

