for value in range(1, 5+1):
    print(value)

numbers = list(range(1, 6))
print(numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

#better version of code above:
squares = []
for value in range(1,15):
    squares.append(value**2)
print(squares)


squares = [value**2 for value in range(1, 11)]
print(squares)
