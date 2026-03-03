# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        def dfs(root, level = 1):
            if not root: return level
            if not root.left and not root.right: return level
            return max(
                dfs(root.left, level + 1),
                dfs(root.right, level + 1)
            )

        return dfs(root, 1)

        