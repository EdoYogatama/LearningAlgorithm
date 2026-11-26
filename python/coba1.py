def minDolls(dollList):
    minVal = min(dollList)
    dollList, xMin = removeAll(dollList, minVal)
    ocurancesDict = {}
    temp = -1
    for i,x in enumerate(dollList):
        if x>minVal:
            if x not in ocurancesDict:
                ocurancesDict[x] = 1
            else:
                ocurancesDict[x] = ocurancesDict[x] + 1    
            
            if ocurancesDict[x]>xMin:
                temp = x
                if i+1<len(dollList):
                    if dollList[i+1]==temp:
                        xMin = xMin + 1
                else: 
                    ocurancesDict[i] = 0
                    xMin = xMin + 1

    return xMin

    
def removeAll(dollList, minVal):
    res = []
    tot = 0
    for i in dollList:
        if i != minVal:
            res.append(i)
        else:
            tot = tot + 1
    return res, tot

print(minDolls([4,2,2,3,3,3,3]))