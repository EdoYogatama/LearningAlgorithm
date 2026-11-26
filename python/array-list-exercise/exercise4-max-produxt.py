def max_product(arr):
    max1, max2 = 0, 0
    for n in arr:
        if n>max1:
            max2 = max1
            max1 = n
        elif n > max2:
            max2 = n

    return max1 * max2

# def max_product(arr):
#     comp = -100
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if comp < arr[i]*arr[j]:
#                 comp = arr[i]*arr[j]

#     return comp

arr = [1, 7, 3, 4, 9, 5]
print(max_product(arr))