#no inbuilts from scratch
class HashTable:
    def __init__(self, size):
        #initalize size 
        self.size = size
        #create empty table
        self.table = [[] for _ in range(size)]

    
    def _hash_function(self, key):
        # Hash function to determine the index for a given key
        return hash(key) % self.size
    
    def insert(self, key, value):
        #insert a key-value pair into hash table
        index = self._hash_function(key)
        #check if key exists in list
        for pair in self.table[index]:
            if pair[0] == key:
                #if key exists, update value
                pair[1] = value
                return
        #if key doesnt exist, append a new key-value pair
        self.table[index].append([key, value])


    def get(self, key):
        #retrieve value associated with given key
        index = self._hash_function(key)
        #search for key in the list at index
        for pair in self.table[index]:
            if pair[0] == key:
                #return the value if key is found
                return pair[1]
        #raise keyerror if key not found
        raise KeyError(key)
    
    def remove(self, key):
        #remove key-value pair from hash table
        index=self._hash_function(key) #get index for the key
        #search for the key in the list at the index
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                #delete the key value pair if key is found
                del self.table[index][i]
                return
            
            #raise keyerror if key is not found
            raise KeyError(key)

#test
hash_table = HashTable(10)
hash_table.insert("apple", 5)
hash_table.insert("banana", 7)
print(hash_table.get("apple"))  # Output: 5
print(hash_table.get("banana")) # Output: 7

#remove value 
hash_table.remove("apple")
try:
    print(hash_table.get("apple"))
except KeyError as e:
    print("KeyError:", e)  # Output: KeyError: 'apple'





