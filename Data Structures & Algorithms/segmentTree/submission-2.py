class Node:
    def __init__(self, L, R, sum=0):
        self.L = L
        self.R = R
        self.sum = sum
        self.left = None
        self.right = None

class SegmentTree:
    
    def __init__(self, nums: List[int]):
        L = 0
        R = len(nums) - 1
        self.nums = nums
        self.root = self.build(L, R)

    def build(self, L, R):
        if L == R:
            return  Node(L, R, self.nums[L])
        root = Node(L, R)
        M = (L + R) // 2
        root.left = self.build(L, M)
        root.right = self.build(M + 1, R)
        root.sum = root.left.sum + root.right.sum
        return root
            
    def update(self, index: int, val: int) -> None:
        self.update_rec(index, val, self.root)
    
    def update_rec(self, index, val, root):
        if index == root.L and index == root.R:
            root.sum = val
            return
        M = (root.L + root.R) // 2
        if index > M:
            self.update_rec(index, val, root.right)
        else:
            self.update_rec(index, val, root.left)
        root.sum = root.left.sum + root.right.sum

    
    def query(self, L: int, R: int) -> int:
        return self.query_rec(L, R, self.root)

    def query_rec(self, L, R, root) -> int:
        if root.L == L and root.R == R:
            return root.sum
        M = (root.L + root.R) // 2
        if R <= M:
            return self.query_rec(L, R, root.left)
        if M < L:
            return self.query_rec(L, R, root.right)
        return self.query_rec(L, M, root.left) + self.query_rec(M + 1, R, root.right)    

