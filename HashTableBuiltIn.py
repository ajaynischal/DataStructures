# Creating a dictionary
my_dict = {"apple": 5}

# Accessing values using keys
print(my_dict["apple"])  # Output: 5

# Adding a new key-value pair
my_dict["grape"] = 9

# Removing a key-value pair
del my_dict["apple"]

# Iterating over keys and values
for key, value in my_dict.items():
    print(key, "->", value)
