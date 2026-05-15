# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max = float('-inf')
        self.dfs(root)
        return int(self.max)
    
    def dfs(self, root):
        if root == None:
            return 0
        
        maxL = self.dfs(root.left)
        maxR = self.dfs(root.right)

        maxLR = maxL + maxR + root.val
        self.max = max(maxLR, self.max)

        newSingleMax = max(maxL, maxR) + root.val

        return newSingleMax
