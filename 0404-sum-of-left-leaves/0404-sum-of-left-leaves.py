# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        summ = 0
        def dfs(node, direction):
            nonlocal summ
            if not node.left and not node.right:
                if direction == 'left':
                    summ += node.val
                return
            
            if node.left:
                dfs(node.left, 'left')
            if node.right:
                dfs(node.right, 'right')
        
        dfs(root, 'root')

        return summ
            
