# 4-3. Counting to Twenty:
print("Exercise 4-3: Counting to Twenty")
for number in range(1, 21):
    print(number)
print()

# 4-4. One Million:
#print("Exercise 4-4: One Million")
#numbers = list(range(1, 1000001))
#for number in numbers:
#    print(number)
# Note: This might take a while to print a million numbers, and you can stop it manually.
#print()

# 4-5. Summing a Million:
print("Exercise 4-5: Summing a Million")
numbers = list(range(1, 1000001))
print("Min:", min(numbers))
print("Max:", max(numbers))
print("Sum:", sum(numbers))
print()

# 4-6. Odd Numbers:
print("Exercise 4-6: Odd Numbers")
odd_numbers = list(range(1, 21, 2))
for number in odd_numbers:
    print(number)
print()

# 4-7. Threes:
print("Exercise 4-7: Threes")
multiples_of_three = list(range(3, 31, 3))
for number in multiples_of_three:
    print(number)
print()

# 4-8. Cubes:
print("Exercise 4-8: Cubes")
cubes = [number**3 for number in range(1, 11)]
for cube in cubes:
    print(cube)
print()

# 4-9. Cube Comprehension:
print("Exercise 4-9: Cube Comprehension")
cubes = [number**3 for number in range(1, 11)]
print(cubes)
