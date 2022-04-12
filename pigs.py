bricks = input("please enter a 3 digits number: ")
bricks = int(bricks)

hundreds = (bricks // 100)
print(hundreds)
tens = ((bricks % 100) // 10)
print(tens)
units = (bricks % 10)
print(units)
alls = (hundreds + tens + units)

print(alls)

print(alls // 3)

print(alls % 3)

first = bool(alls // 3 )
print(first == True)
second = bool(alls % 3)
#print(first == second or first != second)
print(second == False )