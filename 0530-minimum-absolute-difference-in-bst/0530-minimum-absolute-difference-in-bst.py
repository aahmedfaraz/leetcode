# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        diff = float('inf')

        que = [root]
        vals = []

        def dfs(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [root.val]
            vals = []
            if root.left:
                vals.extend(dfs(root.left))
            vals.append(root.val)
            if root.right:
                vals.extend(dfs(root.right))
            return vals

        vals = dfs(root)

        for i in range(len(vals)-1):
            diff = min(diff, vals[i+1] - vals[i])
    
        return diff
            

