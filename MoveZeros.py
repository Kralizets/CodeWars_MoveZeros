def move_zeros(array):
    result = []
    countZero = 0

    for elem in array:
        if (elem == 0):
            countZero += 1
            continue
        result.append(elem)

    for i in range(countZero):
        result.append(0)

    return result

array1 = [1, 2, 3, 4, 10]
array2 = [0, 1, 0, 2, 0]
array3 = [0, 0, 0]
array4 = [1, 2, 3, 0, 2, 0]

res1 = move_zeros(array1)
res2 = move_zeros(array2)
res3 = move_zeros(array3)
res4 = move_zeros(array4)