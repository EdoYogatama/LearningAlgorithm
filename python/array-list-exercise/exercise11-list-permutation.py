def isPermutation(arr1, arr2):
    if len(arr1)!=len(arr2):
        return False
    
    for x in arr1:
        for y in arr2:
            if y == x:
                arr2.remove(x)
            

    if len(arr2)>0:
        return False
    else:
        return True
    
print(isPermutation([1,2,3],[2,3,1]))