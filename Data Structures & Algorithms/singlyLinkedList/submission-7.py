class ListNode:
    def __init__(self, nextNode, value: int):
        self.nextNode = nextNode
        self.value = value

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    
    def get(self, index: int) -> int:
        current = self.head
        i = 0
        while current and i < index:
            current = current.nextNode
            i += 1
        if current and i == index:
            return current.value
        return -1
        

    def insertHead(self, val: int) -> None:
        newHead = ListNode(self.head, val)
        if self.head == None:
            self.tail = newHead
        self.head = newHead
        

    def insertTail(self, val: int) -> None:
        newTail = ListNode(None, val)
        if self.head == None:
            self.tail = newTail
            self.head = newTail
        else:
            self.tail.nextNode = newTail
            self.tail = newTail
        

    def remove(self, index: int) -> bool:
        if index == 0 and self.head != None:
            self.head = self.head.nextNode
            return True
        current = self.head
        i = 0
        while current and i + 1 < index:
            current = current.nextNode
            i += 1
        if current == None or current.nextNode == None:
            return False
        if current.nextNode == self.tail:
            self.tail = current
        current.nextNode = current.nextNode.nextNode
        return True
        

    def getValues(self) -> List[int]:
        current = self.head
        arr = []
        while current:
            arr.append(current.value)
            current = current.nextNode
        return arr
        
