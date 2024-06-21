from array import *
# SECTION : CREATE AN ARRAY 
# import array
# my_array = array('i')
# print(my_array)
# my_array = array('i', [1,2,3,4,5])
# print(my_array)

# import numpy as np
# np_array = np.array([], dtype=int)
# print(np_array)
# np_array1 = np.array([1,2,3,4,5])

# SECTION : INSERTION TO OPERATION
# my_array = array('i', [1,2,3,4,5])
# print(my_array)

# my_array.insert(0, 6)
# print(my_array)

# SECTION : TRAVERSAL OPERATION

# arr1 = array('i', [1,2,3,4,5,6])
# arr2 = array('d', [1.3, 1.5, 1.6])
# arr1.insert(2,9)
# print(arr1)
# print(arr2)

# def traverseArray(array):
#     for i in array:
#         print(i)

# traverseArray(arr1)

# SECTION : ACCESSING ARRAY

# arr1 = array('i', [1,2,3,4,5,6])

# def accessElement(array, index):
#     if index > len(array):
#         print("Exception")
#     else:
#         print(array[index])

# accessElement(arr1, 8)

# SECTION : SEARCH IN ARRAY -> Linier Search
# arr1 = array('i', [1,2,3,4,5,6])

# def linier_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i]==target:
#             return i
#     return -1

# print(linier_search(arr1, 4))

# SECTION : DELETE ELEMENT
# arr1 = array('i', [1,2,3,4,5,6])

# arr1.remove(4)

# print(arr1)

# SECTION : PRACTICE

# 1. Create an array and traverse -> O(n)
print("Step 1")
myArray = array('i', [1,2,3,4,5])
for i in myArray:
    print(i)

# 2. Acces individual elements through indexes
print("Step 2")
print(myArray[3])    

# 3. Append any value to the array using append method -> O(1)
print("Step 3")
myArray.append(6)
print(myArray)

# 4. insert valuue in an array using insert method
print("Step 4")
myArray.insert(3, 11)
print(myArray)

# 5. Extend python array using extend method
print("Step 5")
myArray1 = array('i', [10,11,12])
myArray.extend(myArray1)
print(myArray)

# 6. add item from list into array using fromlist method
print("Step 6")
tempList = [20,21,22]
myArray.fromlist(tempList)
print(myArray)

# 7. remove any array element using remove method
print("Step 7")
myArray.remove(20) # remove first occurance
print(myArray)

# 8. Remove last array element using pop method
print("Step 8")
myArray.pop()
print(myArray)

# 9. fetch any element through its index using index method
print("Step 9")
print(myArray.index(10))

# 10. reverse an array using reverse method
print("Step 10")
myArray.reverse()
print(myArray)

# 11. get array buffer information through buffer_info method
print("Step 11")
print(myArray.buffer_info())

# 12. check for number og occurances of an element using count method
print("Step 12")
print(myArray.count(11))

# 13. convert array to string using tostring method
print("Step 13")
strTemp = myArray.tobytes()
print(strTemp)
bkArray = array('i')
bkArray.frombytes(strTemp)
print(bkArray)

# 14. convert array to a python list with same elements using tolist method
print("Step 14")
print(myArray.tolist())

# 15. appen a string to char array using fromstring method
print("Step 15 -> refer to Step 13")

# 16. slice elements from an array
print("Step 16")
print(myArray[1:4])