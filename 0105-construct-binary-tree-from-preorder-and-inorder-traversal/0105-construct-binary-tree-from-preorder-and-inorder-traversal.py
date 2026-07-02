# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        rootval = preorder[0]
        rootAt = inorder.index(rootval)
        
        preorderLeft = preorder[1 : rootAt+1]
        preorderRight = preorder[rootAt+1 :]

        inorderLeft = inorder[: rootAt]
        inorderRight = inorder[rootAt+1 :]
        
        return TreeNode(rootval, self.buildTree(preorderLeft, inorderLeft), self.buildTree(preorderRight, inorderRight))