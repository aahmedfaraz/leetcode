# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right: return True
        if (root.left and not root.right) or (not root.left and root.right): return False

        left = root.left
        right = root.right

        def dfs(r1, r2):
            if not r1 and not r2: return True
            if (r1 and not r2) or (r2 and not r1): return False
            if r1.val != r2.val: return False

            return dfs(r1.left, r2.right) and dfs(r1.right, r2.left)

        return dfs(left, right)