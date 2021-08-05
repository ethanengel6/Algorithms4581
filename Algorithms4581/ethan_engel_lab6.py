
# HashTable ADT with chaining implementation
# This hashtable accepts only strings and hashes based on their
# ASCII value of the first char
# The constructor takes in the size of the table
class MyHashtable(object):
    def __init__ (self, size): # Creates an empty hashtable
        self.size = size
# Create the list (of size) of empty lists (chaining)
        self.table = []
        for i in range(self.size):
            self.table.append([])
    def __str__ (self): # for print
        return str(self.table)
    def insert(self, elem): # Adds an element into the hashtable
        hash = ord(elem[0]) % self.size
        self.table[hash].append(elem)
    def member(self, elem): # Returns if element exists in hashtable
        hash = ord(elem[0]) % self.size
        return elem in self.table[hash]
    def delete(self, elem): # Removes an element from the hashtable
        hash = ord(elem[0]) % self.size
        self.table[hash].remove(elem)

class OpenHash(object):
    def __init__(self,size):
        self.size = size
        self.table = [None]*self.size
        self.status=["Empty"]*self.size

    def __str__(self):
        return str(self.table)

    def insert(self, elem): # Adds an element into the hashtable
        hash = ord(elem[0]) % self.size
        while True:
            if self.status[hash]!="Filled":
                self.table[hash]=elem
                self.status[hash]= "Filled"
                break
            elif hash==self.size-1:
                hash=0
            else:
                hash+=1

    def delete(self, elem): # Removes an element from the hashtable
        hash = ord(elem[0]) % self.size
        for zz in range (self.size):
            if self.table[hash]==elem:
                self.table[hash]=None
                self.status[hash]= "Deleted"
                break
            elif self.status[hash]=="Empty":
                break
            elif hash==self.size-1:
                hash=0
            else:
                hash +=1

    def member(self, elem):
        hash = ord(elem[0]) % self.size
        for qq in range (self.size):
            if self.table[hash]==elem:
                return True
            elif self.status[hash]=="Empty":
                return False
            elif hash==self.size-1:
                hash=0
            else:
                hash +=1


# Testing code
s = OpenHash(10)
s.insert("amy") #97
s.insert("chase") #99
s.insert("chris") #99
print(s.member("amy"))
print(s.member("chris"))
print(s.member("alyssa"))
s.delete("chase")
print(s.member("chris"))
print(s)
