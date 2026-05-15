# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, -10000, 10000)
    
    def dfs(self, root, min_val, max_val):
        if not root:
            return True

        l, r = min_val - 1, max_val + 1
        if root.left:
            l = root.left.val
        if root.right:
            r = root.right.val
        
        print(l, min_val, root.val, max_val, r)
        valid = True
        if min_val != -10000:
            valid = l < min_val < root.val
        if max_val != 10000:
            valid = root.val < max_val < r
        valid = valid and l < root.val < r

        return valid and self.dfs(root.left, min_val, root.val) and self.dfs(root.right, root.val, max_val)
        