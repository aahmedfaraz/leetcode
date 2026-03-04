# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        def getHeight(root):
            if not root: return 0
            if not root.left and not root.right: return 1
            left = 1 + getHeight(root.left)
            right = 1 + getHeight(root.right)
            return max(left, right)

        leftHeight = getHeight(root.left)
        rightHeight = getHeight(root.right)

        return abs(leftHeight-rightHeight) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)