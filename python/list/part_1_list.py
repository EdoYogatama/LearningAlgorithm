'''
list holds an ordered collection of item
'''

# Traversal
shoppingList = ['Milk', 'Cheese', 'Butter']
print(shoppingList[2])
print('Milk' in shoppingList)
print(shoppingList[-2])
for i in shoppingList:
    print(i)
for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i] + '+'
    print(shoppingList[i])
empty = []
for i in empty:
    print("I am empty")

# Update/Insert
myList = [1,2,3,4,5,6,7]
print(myList)
myList[2] = 33
myList[4] = 55
print(myList)
## insert()
myList.insert(0, 11)
print(myList)
## append()
myList.append(55)
print(myList)
## extend()
newList = [11,12,13,14]
myList.extend(newList)
print(myList)

# Delete/Slice
myList = ['a', 'b', 'c', 'd', 'e', 'f']
print(myList[0:2])
print(myList[:2])
myList[0:2] = ['x', 'y']
print(myList)
myList.pop(1)
print(myList)
myList.pop()
print(myList)
del myList[:1]
print(myList)
myList.remove('e')
print(myList)

# Search
myList = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target = 50
if target in myList:
    print(f"{target} is in the list")
else:
    print(f"{target} is not in list")
## Liner Search
def linear_search(ll, target):
    for i, value in enumerate(ll):
        if value == target:
            return i
    return -1
print(linear_search(myList, target))

# List Operation
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)

a = [0,1]
a = a * 4
print(a)

a = [1,2,3,4,5,6]
print(len(a))
print(max(a))
print(min(a))
print(sum(a))
print(sum(a)/len(a))