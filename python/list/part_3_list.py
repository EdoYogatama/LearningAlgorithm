prev = [1,2,3]
new = [i*2 for i in prev]

print(new)

prev = [-1,-2,-3,-4,-5,-6,-7,-8, 11, 2, 1]
new = [number for number in prev if number>0]

print(new)

prev = [-1,-2,-3,-4,-5,-6,-7,-8, 11, 2, 1]
new = [number*number for number in prev if number<0]

print(new)

sentence = "My name is Elshad"
def isConsonant(letter):
    vowels = 'aiueo'
    return letter.isalpha() and letter.lower() not in vowels

consonant = [i for i in sentence if isConsonant(i)]
print(consonant)

prev = [-1,10,-26,2,-98,60,45,20]
new = [number if number > 0 else 0 for number in prev]
print(new)