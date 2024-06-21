def pair_sum(myList, sum):
    res = []
    for i in range(len(myList)):
        number1 = myList[i]
        for j in range(i+1, len(myList)):
            if sum == number1+myList[j]:
                number2 = myList[j]
                res.append(str(number1)+'+'+str(number2))

    return res

print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))