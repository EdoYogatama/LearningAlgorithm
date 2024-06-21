def diagonal_sum(matrix):
    sum = 0

    for i in range(len(matrix)):
        sum = sum + matrix[i][i]

    return sum

# def diagonal_sum(matrix):
#     sum = 0
#     idx = 0

#     for list in matrix:
#         sum = sum + list[idx]
#         idx += 1

#     return sum

myList2D = [[1,2,3],[4,5,6],[7,8,9]]
print(diagonal_sum(myList2D))