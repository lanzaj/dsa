class Node:
    def __init__(self, key:int, val:int):
        self.key = key
        self.val = val
        self.right = None
        self.left = None

class TreeMap:
    
    def __init__(self):
        self.map = None

    def insert(self, key: int, val: int) -> None:
        if not self.map:
            self.map = Node(key, val)
            return
        current = self.map
        while current:
            if key < current.key:
                if current.left == None:
                    current.left = Node(key, val)
                    return
                current = current.left
            elif key > current.key:
                if current.right == None:
                    current.right = Node(key, val)
                    return
                current = current.right
            else:
                current.val = val
                return


    def get(self, key: int) -> int:
        if not self.map:
            return -1
        current = self.map
        while current:
            if current.key < key:
                current = current.left
            elif current.key > key:
                current = current.right
            else:
                return current.val
        return -1

    def getMin(self) -> int:
        if not self.map:
            return -1
        current = self.map
        while current.left:
            current = current.left
        return current.val
    
    def getMinNode(self, head: Node) -> Optional[Node]:
        if not head or not head.left:
            return head
        current = head
        while current.left:
            current = current.left
        return current

    def getMax(self) -> int:
        if not self.map:
            return -1
        current = self.map
        while current.right:
            current = current.right
        return current.val

    def remove(self, key: int) -> None:
        self.map = self.deleteNode(key, self.map)

    def deleteNode(self, key:int , node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None
        if key < node.key:
            node.left = self.deleteNode(key, node.left)
        elif key > node.key:
            node.right = self.deleteNode(key, node.right)
        else:
            if node.left == None:
                return node.right
            if node.right == None:
                return node.left
            minimum = self.getMinNode(node.right)
            node.key = minimum.key
            node.val = minimum.val
            node.right = self.deleteNode(minimum.key, node.right)
        return node


    def getInorderKeys(self) -> List[int]:
        ret = []
        def getKeys(node: Optional[Node]):
            nonlocal ret
            if not node:
                return
            getKeys(node.left)
            ret.append(node.key)
            getKeys(node.right)
        getKeys(self.map)
        return ret

