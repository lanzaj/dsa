class HashTable:
    
    def __init__(self, capacity: int):
        self.hashTable = [None for _ in range(capacity)]
        self.capacity = capacity
        self.size = 0

    def insert(self, key: int, value: int) -> None:
        i = key % self.capacity
        while self.hashTable[i] != None:
            if self.hashTable[i] != None:
                currKey, currVal = self.hashTable[i]
                if currKey == key:
                    self.hashTable[i] = (key, value)
                    return
            i = (i + 1) % self.capacity
        self.hashTable[i] = (key, value)
        self.size += 1
        if self.size * 2 >= self.capacity:
            self.resize()

    def get(self, key: int) -> int:
        i = key % self.capacity
        while self.hashTable[i] != None:
            currKey, currVal = self.hashTable[i]
            if currKey == key:
                return currVal
            i = (i + 1) % self.capacity
        return -1

    def remove(self, key: int) -> bool:
        i = key % self.capacity
        while self.hashTable[i] != None:
            currKey, currVal = self.hashTable[i]
            if currKey == key:
                self.hashTable[i] = None
                return True
            i = (i + 1) % self.capacity
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        oldHashTable = self.hashTable
        self.size = 0
        self.hashTable = [None for _ in range(self.capacity)]
        for element in oldHashTable:
            if element != None:
                key, val = element
                self.insert(key,val)

