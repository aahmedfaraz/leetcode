# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, direction, summ):
            if not node.left and not node.right:
                if direction == 'left':
                    summ += node.val
                return summ
            new_sum = 0
            if node.left:
                new_sum += dfs(node.left, 'left', summ)
            if node.right:
                new_sum += dfs(node.right, 'right', summ)

            return new_sum
        
        return dfs(root, 'root', 0)