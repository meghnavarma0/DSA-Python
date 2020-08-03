# Design a HashSet without using any built-in hash table libraries.

# To be specific, your design should include these functions:

# add(value): Insert a value into the HashSet. 
# contains(value) : Return whether the value exists in the HashSet or not.
# remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

# Example:

# MyHashSet hashSet = new MyHashSet();
# hashSet.add(1);         
# hashSet.add(2);         
# hashSet.contains(1);    // returns true
# hashSet.contains(3);    // returns false (not found)
# hashSet.add(2);          
# hashSet.contains(2);    // returns true
# hashSet.remove(2);          
# hashSet.contains(2);    // returns false (already removed)

class MyHashSet:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = [0 for i in range(10000001)]
        

    def add(self, key: int) -> None:
        self.hash[key] = 1
        
        

    def remove(self, key: int) -> None:
        if self.hash[key] > 0:
            self.hash[key] = 0
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if self.hash[key] > 0:
            return True
        return False