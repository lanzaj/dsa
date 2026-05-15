class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    def __init__(self):
        self.map = None

    def insert(self, key: int, val: int) -> None:
        newNode = Node(key, val)
        if not self.map:
            self.map = newNode
            return
        current = self.map
        while True:
            if key < current.key:
                if not current.left:
                    current.left = newNode
                    return
                current = current.left
            elif key > current.key:
                if not current.right:
                    current.right = newNode
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
            if key < current.key:
                current = current.left
            elif key > current.key:
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


    def getMax(self) -> int:
        if not self.map:
            return -1
        current = self.map
        while current.right:
            current = current.right
        return current.val


    def remove(self, key: int) -> None:

        def getMinNode(self) -> int:
            if not self.map:
                return -1
            current = self.map
            while current.left:
                current = current.left
            return current

        def deleteNode(node: Node) -> Node:
            if not self.map:
                return
            current = self.map
            while current:
                if key < current.key:
                    current.left = deleteNode(current.left)
                elif key > current.key:
                    current.right = deleteNode(current.right)
                else:
                    if not current.left:
                        return current.right
                    elif not current.right:
                        return current.left
                    else:
                        minimum = getMinNode(current.right)
                        current.val = minimum.val
                        current.key = minimum.key
                        current.right = deleteNode(current.right)
                        return current
                return current

        self.map = deleteNode(self.map)

    def getInorderKeys(self) -> List[int]:
        ret = []

        def getKeys(node: Node):
            nonlocal ret
            if not node:
                return
            if node.left:
                getKeys(node.left)
            ret.append(node.key)
            if node.right:
                getKeys(node.right)

        getKeys(self.map)

        return ret

