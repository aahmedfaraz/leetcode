# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root: return None
        if not root.left and not root.right: return root
        if root.right:
            root.right = self.flatten(root.right)
        if root.left:
            root.left = self.flatten(root.left)
            curr = root.left
            while curr.right:
                curr = curr.right
            curr.right = root.right
            root.right = root.left
            root.left = None
        return root