def remove_duplicate(arr):
    unique = []
    seen = set()
    for item in arr:
        if item not in seen:
            unique.append(item)
            seen.add(item)

    return unique

# def remove_duplicate(arr):
#     dist = []
#     for i in arr:
#         if i not in dist:
#             dist.append(i)

#     return dist

myArr = [1,1,2,3,2,3,4,5]
print(remove_duplicate(myArr))