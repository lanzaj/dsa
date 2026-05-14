class MinHeap:
    
    def __init__(self):
        self.heap = [0]

    def fix(self, index: int) -> None:
        if index == 1:
            return
        if self.heap[index] < self.heap[index // 2]:
            self.heap[index], self.heap[index //2] = self.heap[index //2 ], self.heap[index]
            self.fix(index // 2)

    def push(self, val: int) -> None:
        self.heap.append(val)
        self.fix(len(self.heap) - 1)

    def fixDown(self, i: int) -> None:
        if i * 2 >= len(self.heap):
            return
        elif i * 2+1 >= len(self.heap):
            if self.heap[i] > self.heap[i*2]:
                self.heap[i], self.heap[i*2] = self.heap[i*2], self.heap[i]
                return
        elif self.heap[i] > self.heap[i*2] or self.heap[i] > self.heap[i*2 + 1]:
            if i*2 + 1 >= len(self.heap):
                self.heap[i], self.heap[i*2] = self.heap[i*2], self.heap[i]
            elif self.heap[i*2] < self.heap[i*2 + 1]:
                self.heap[i], self.heap[i*2] = self.heap[i*2], self.heap[i]
                self.fixDown(i*2)
            else:
                self.heap[i], self.heap[i*2+1] = self.heap[i*2+1], self.heap[i]
                self.fixDown(i*2+1)   

    def pop(self) -> int:
        if len(self.heap) == 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()
        popValue = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.fixDown(1)
        return popValue
        

    def top(self) -> int:
        if len(self.heap) <=1:
            return -1
        return self.heap[1]

    def heapify(self, nums: List[int]) -> None:
        self.heap = [0] + nums
        for i in range((len(nums) - 1)//2, 0, -1):
            self.fixDown(i)
        
        