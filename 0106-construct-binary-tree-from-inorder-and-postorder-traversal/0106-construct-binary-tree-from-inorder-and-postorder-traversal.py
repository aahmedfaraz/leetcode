# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        
        inmap = {val: i for i, val in enumerate(inorder)}

        def bT(inL, inR, pL, pR):
            if inL > inR:
                return None
            if inL == inR:
                return TreeNode(postorder[pL])

            rootval = postorder[pR]
            rootat = inmap[rootval]
            leftsize = rootat - inL

            return TreeNode(rootval, bT(inL, inL+leftsize-1, pL, pL+leftsize-1), bT(inL+leftsize+1, inR, pL+leftsize, pR-1))
            
        
        n = len(inorder)
        return bT(0, n-1, 0, n-1)