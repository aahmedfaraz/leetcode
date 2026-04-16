# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        summ = 0
        stack = [root]
        while stack:
            node = stack.pop()

            if node.left:
                if not node.left.left and not node.left.right:
                    summ += node.left.val
                else:
                    stack.append(node.left)
            if node.right:
                if node.right.left or node.right.right:
                    stack.append(node.right)

        return summ
                