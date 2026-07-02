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
        inmap = {val: i for i, val in enumerate(inorder)}

        def builtT(s1, g2, h4, k9): # to increase the challenge, renaming for myself
            if s1 > g2:
                return None
            if s1 == g2:
                return TreeNode(preorder[s1])

            rootval = preorder[s1]
            rootat = inmap[rootval]
            lsize = rootat - h4

            root = TreeNode(rootval)

            root.left = builtT(
                s1+1,
                s1+lsize,
                h4,
                rootat-1,
            )
            root.right = builtT(
                s1+lsize+1,
                g2,
                rootat+1,
                k9,
            )

            return root

        return builtT(0, len(preorder)-1, 0, len(inorder)-1)