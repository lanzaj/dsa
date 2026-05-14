class DynamicArray:
    
    def __init__(self, capacity: int):
        self.dynamic_array = [0 for _ in range(capacity)]
        self.size = 0
        self.capacity = capacity


    def get(self, i: int) -> int:
        return self.dynamic_array[i]


    def set(self, i: int, n: int) -> None:
        self.dynamic_array[i] = n


    def pushback(self, n: int) -> None:
        if self.size + 1 > self.capacity:
            self.resize()
        self.dynamic_array[self.size] = n
        self.size += 1


    def popback(self) -> int:
        self.size -= 1
        return self.dynamic_array[self.size]
 

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        new_array = [0 for _ in range(self.capacity)]
        for i, n in enumerate(self.dynamic_array):
            new_array[i] = n
        self.dynamic_array = new_array


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
