arr = []
for i in range(3):
    x = []
    x = input().split()

    arr.append(x)

for i in range(3):
    for j in range(3):
        print(arr[j][i], end = " ")
    print()