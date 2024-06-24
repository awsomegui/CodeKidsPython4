double = lambda x: x * 2

print(double(24))

square = lambda x: x ** 2

print(square(16))

numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21]

print(numbers)

#for index in range(len(numbers)):
#    numbers[index] = square(numbers[index])

#print(numbers)

squaredList = list(map(square, numbers))
doubledList = list(map(double, numbers))
halvedList = list(map(lambda x: x / 2, numbers))
doubledandaddoneList = list(map(lambda x: x * 2 + 1, numbers))
print(squaredList)
print(doubledList)
print(halvedList)
print(doubledandaddoneList)

evenList = list(filter(lambda x: x % 2 == 0, numbers))
oddList = list(filter(lambda x: x % 2 != 0, numbers))

print(evenList)
print(oddList)

names = ["Henry", "Bob", "Fred", "James"]
bannedNames = ["Henry", "James"]
cleanNames = filter(lambda x: x not in bannedNames, names)

print(list(cleanNames))