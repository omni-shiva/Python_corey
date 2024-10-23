#**NOTE**

"""*args is used for passing non-keyword variable-length arguments (as a tuple).
**kwargs is used for passing keyword variable-length arguments (as a dictionary)."""

#1 . --------args-----------
"""*args allows you to pass a variable number of non-keyword arguments to a function.
Inside the function, args will be a tuple of all the additional arguments passed."""
# Example:

def greet(*args):
    for name in args:
        print(f"Hello, {name}!")

greet("Alice", "Bob", "Charlie")

#Output
# Hello, Alice!
# Hello, Bob!
# Hello, Charlie!


#2 . **kwargs
"""**kwargs allows you to pass a variable number of keyword arguments to a function.
Inside the function, kwargs will be a dictionary of all the additional keyword arguments passed."""

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")

# Output
# name: Alice
# age: 30
# city: New York


# Combined 
"""*args and **kwargs
You can use both *args and **kwargs in the same function if needed:

"""


def mix(*args, **kwargs):
    print("Non-keyword arguments:", args)
    print("Keyword arguments:", kwargs)

mix(1, 2, 3, name="Alice", age=30)

#output
"""Non-keyword arguments: (1, 2, 3)
Keyword arguments: {'name': 'Alice', 'age': 30}
"""


