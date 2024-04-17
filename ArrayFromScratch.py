class Array:
    def __init__(self, size):
        # Initialize an array with a specified size
        self.size = size
        self.data = [None] * size

    def __getitem__(self, index):
        # Get the value at a specific index
        if 0 <= index < self.size:
            return self.data[index]
        else:
            raise IndexError("Index out of range")

    def __setitem__(self, index, value):
        # Set the value at a specific index
        if 0 <= index < self.size:
            self.data[index] = value
        else:
            raise IndexError("Index out of range")

# Example usage:
arr = Array(5)
arr[0] = 1
arr[1] = 2
arr[2] = 3
print(arr[0])  # Output: 1
print(arr[1])  # Output: 2
print(arr[2])  # Output: 3



