# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, -10001, 10001 )[0]
    
    def dfs(self, root: Optional[TreeNode], min_val, max_val) -> list:
        if not root:
            return [True, min_val, max_val]
        retL, minL, maxL = self.dfs(root.left, min_val, root.val)
        retR, minR, maxR = self.dfs(root.right, root.val, max_val)
        
        is_valid = retL and retR
        if root.left:
            if root.left.val >= root.val or root.left.val <= min_val:
                is_valid = False
        if root.right:
            if root.right.val <= root.val or root.right.val >= max_val:
                is_valid = False
        
        return [is_valid, min_val, max_val]