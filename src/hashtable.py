# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        arrayIndex = self._hash_mod(key)
        keyAlreadyExists = False
        nodePtr = None
         
        if self.storage[arrayIndex] != None:
            # Check if the key already exists within the asociated link list
            nodePtr = self.storage[arrayIndex]
            if nodePtr.key == key:
                keyAlreadyExists = True
            while nodePtr.next != None and not keyAlreadyExists:
                nodePtr = nodePtr.next
                if nodePtr.key == key:
                    keyAlreadyExists = True

            if keyAlreadyExists:
                nodePtr.value = value
            else:
                newNode = LinkedPair(key,value)
                nodePtr.next = newNode
        else:
            # The key does not exist becasue the asociated link list does not exist
            newNode = LinkedPair(key,value)
            self.storage[arrayIndex] = newNode

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        pass


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        arrayIndex = self._hash_mod(key)
        keyAlreadyExists = False
        nodePtr = None
         
        if self.storage[arrayIndex] != None:
            # Check if the key already exists within the asociated link list
            nodePtr = self.storage[arrayIndex]
            if nodePtr.key == key:
                keyAlreadyExists = True
            while nodePtr.next != None and not keyAlreadyExists:
                nodePtr = nodePtr.next
                if nodePtr.key == key:
                    keyAlreadyExists = True

            if keyAlreadyExists:
                return nodePtr.value
            else:
                return None
        else:
            # The key does not exist becasue the asociated link list does not exist
            return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        pass



if __name__ == "__main__":
    ##########################################################################
    # My printing function for hash table
    ##########################################################################
    # def printHt(ht):
    #     for elem in ht.storage:
    #         if elem == None:
    #             print("None")
    #         else:
    #             print("Used",end="")
    #             currNode = elem
    #             while currNode != None:
    #                 print(f'->({currNode.key},{currNode.value})',end="")
    #                 currNode = currNode.next
    #             print("")

    ##########################################################################
    # Default testing code
    #########################################################################
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")

    
                
    ##########################################################################
    # My testing code
    #########################################################################
    # ht = HashTable(8)

    # ht.insert("key-0", "val-0")
    # ht.insert("key-1", "val-1")
    # ht.insert("key-2", "val-2")
    # ht.insert("key-3", "val-3")
    # ht.insert("key-4", "val-4")
    # ht.insert("key-5", "val-5")
    # ht.insert("key-6", "val-6")
    # ht.insert("key-7", "val-7")
    # ht.insert("key-8", "val-8")
    # ht.insert("key-9", "val-9")

    # print("First printing:")
    # printHt(ht)

    # ht.insert("key-6", "val-NOT6")
    # print("Second printing:")
    # printHt(ht)
    # Note that the hash function uses a random value for every python process for
    # some security issue. If you want to stop it from using a random value for debugging
    # purposes, then set the path variable in the base shell using 'export PYTHONHASHSEED=0'
    # To set it back to use random again, use 'export PYTHONHASHSEED=random', or open up
    # a new shell 
