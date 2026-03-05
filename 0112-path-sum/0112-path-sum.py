# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        foundSum = False
        def dfs(root, currSum):
            nonlocal foundSum
            if foundSum: return 0
            if not root.left and not root.right: 
                currSum += root.val
                if currSum == targetSum:
                    foundSum = True
                return currSum
            if root.left:
                dfs(root.left, currSum + root.val)
            if root.right:
                dfs(root.right, currSum + root.val)
        dfs(root, 0)
        return foundSum