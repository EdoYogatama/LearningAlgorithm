inputList = []
while(True):
    inp = input("Enter a number: ")
    if inp == 'done': break
    inputList.append(float(inp))

print('Average: ', sum(inputList)/len(inputList))