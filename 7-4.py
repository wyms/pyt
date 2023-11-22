# 7-4. Pizza Toppings
topping = ""
while topping != 'quit':
    topping = input("Enter a pizza topping (type 'quit' to finish): ")
    if topping != 'quit':
        print(f"I'll add {topping} to your pizza.")
