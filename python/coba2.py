def maxProfit(M, prices):
    resList = [0] * M

    for i,x in enumerate(resList):
        for v in prices:
            if x>v:
                resList[i] = v
        prices.remove(resList[i])

    def sumUpProfit():
        res = 0
        for i in resList:
            res = res + (i*-1)

        return res
    
    res = sumUpProfit()
    return res

print(maxProfit(1,[-1,-10]))