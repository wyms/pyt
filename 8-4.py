def make_shirt(size="large", message="I love Python"):
    print(f"The shirt is size {size.upper()} and has the message: '{message}'")

# Make a large shirt with default message
make_shirt()

# Make a medium shirt with default message
make_shirt(size="medium")

# Make a shirt of any size with a different message
make_shirt(size="small", message="Coding is awesome!")

# Test with default values
make_shirt()  # Large shirt with default message

# Test with a medium shirt and default message
make_shirt(size="medium")

# Test with a small shirt and a custom message
make_shirt(size="small", message="Coding is awesome!")
