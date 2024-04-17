from array import array

int_array = array('i', [1, 2, 3, 4, 5])

# 'i': Signed integer
# 'I': Unsigned integer
# 'f': Float
# 'd': Double float
# 'b': Signed char
# 'B': Unsigned char
# 'l': Signed long
# 'L': Unsigned long

print(int_array[0]) # output should be 1
print(int_array[1]) # output should be 2
print(int_array[2]) # output should be 3

int_array[0] = 10 #update at index 0
print(int_array[0]) # output should be 10

int_array.append(6) #adding a 6th element

print(int_array) # output should be 1,2,3,4,5,6

removed_element = int_array.pop(2) #removing 3rd element at index 2
print(removed_element) # should print 3
print(int_array) # 10, 2, 4, 5, 6 should be printed

print(len(int_array)) #length should be 5