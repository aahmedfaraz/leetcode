# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        tilt = 0
        def dfs(root):
            nonlocal tilt
            left, right = 0, 0
            if root.left:
                left = root.left.val + dfs(root.left)
            if root.right:
                right = root.right.val + dfs(root.right)
            tilt += abs(left - right)
            return left + right
        dfs(root)
        return tilt
