# LeetCode 48

def rotate(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i,n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for arr in matrix:
        arr.reverse()

    return matrix

# def rotate(matrix):
#     rotated = []
#     point = 0
#     while len(rotated)<len(matrix):
#         temp = []
#         for arr in matrix[::-1]:
#             temp.append(arr[point])
#         rotated.append(temp)
#         point = point + 1

#     return rotated

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))
