# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        maxdiam = 0

        def dfs(root):
            nonlocal maxdiam
            if not root: return 0
            if not root.left and not root.right: return 1
            left = dfs(root.left)
            right = dfs(root.right)
            maxdiam = max(maxdiam, left + right)
            return 1 + max(left, right)

        dfs(root)

        return maxdiam

        