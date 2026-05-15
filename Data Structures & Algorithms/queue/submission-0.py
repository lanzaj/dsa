class Deque_Node:
    def __init__(self, value = 0, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None


    def isEmpty(self) -> bool:
        if self.head == None:
            return True
        return False
        

    def append(self, value: int) -> None:
        newNode = Deque_Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        

    def appendleft(self, value: int) -> None:
        newNode = Deque_Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        

    def pop(self) -> int:
        if self.head == None:
            return -1
        if self.head.next == None:
            tmp = self.head
            self.head = None
            self.tail = None
            return tmp.value
        tmp = self.tail
        self.tail.prev.next = None
        return tmp.value

    def popleft(self) -> int:
        if self.head == None:
            return -1
        if self.head.next == None:
            tmp = self.head
            self.head = None
            self.tail = None
            return tmp.value
        tmp = self.head
        self.head = self.head.next
        return tmp.value
        
