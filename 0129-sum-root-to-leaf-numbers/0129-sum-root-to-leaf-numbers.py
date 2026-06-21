# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root, num):
            nonlocal res
            if not root:
                return
            rootval = str(root.val)
            if not root.left and not root.right:
                res += int(num + rootval)
                return
            if root.left:
                dfs(root.left, num + rootval)
            if root.right:
                dfs(root.right, num + rootval)
        dfs(root, "")
        return res