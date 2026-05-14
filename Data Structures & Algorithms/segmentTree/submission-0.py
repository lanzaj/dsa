class SegmentNode:
    def __init__(self, total: int, L: int, R: int):
        self.sum = total
        self.L = L
        self.R = R
        self.left = None
        self.right = None

class SegmentTree:
    
    def __init__(self, nums: List[int]):
        def build(L: int, R: int) -> SegmentNode:
            if L == R:
                return SegmentNode(nums[L], L, R)
            M = (L + R) // 2
            node = SegmentNode(0, L, R)
            node.left = build(L, M)
            node.right = build(M + 1, R)
            node.sum = node.left.sum + node.right.sum
            return node
        
        self.root = build(0, len(nums) - 1)
    

    def update(self, index: int, val: int) -> None:
        def update_helper(node: SegmentNode) -> None:
            if node.L == node.R:
                node.sum = val
                return
            
            M = (node.L + node.R) // 2
            if index > M:
                update_helper(node.right)
            else:
                update_helper(node.left)
            node.sum = node.right.sum + node.left.sum
        update_helper(self.root)
        
    def query(self, L: int, R: int) -> int:
        def query_helper(node: SegmentNode, L: int, R: int) -> int:
            if node.L == L and node.R == R:
                return node.sum
            
            M = (node.L + node.R) // 2
            if R <= M:
                return query_helper(node.left, L, R)
            elif L > M:
                return query_helper(node.right, L, R)
            else:
                return query_helper(node.left, L, M) + query_helper(node.right, M + 1, R)
        return query_helper(self.root, L, R)

