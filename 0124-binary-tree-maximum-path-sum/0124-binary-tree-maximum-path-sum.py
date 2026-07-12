# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        largest = float('-inf')
        def dfs(root):
            nonlocal largest
            largest = max(largest, root.val)
            if not root.left and not root.right:
                return root.val
            left, right = 0, 0
            if root.left:
                left = dfs(root.left)
            if root.right:
                right = dfs(root.right)
                
            # if this is center
            rootalone = root.val
            rootwithleft = rootalone + left
            rootwithright = rootalone + right
            rootwithboth = rootwithleft + right
            largest = max([largest, rootalone, rootwithleft, rootwithright, rootwithboth])
            maxarm = max(rootalone, rootwithleft , rootwithright)
            return maxarm
        dfs(root)
        return largest

# Time = O(n)
# Space = O(n)