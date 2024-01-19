def make_shirt(size, message):
    print(f"The shirt is size {size.upper()} and has the message: '{message}'")

# Call the function with positional arguments
make_shirt("medium", "Hello, World!")

# Call the function with keyword arguments
make_shirt(size="small", message="Python is fun!")

# Test with positional arguments
make_shirt("medium", "Hello, World!")

# Test with keyword arguments
make_shirt(size="small", message="Python is fun!")
