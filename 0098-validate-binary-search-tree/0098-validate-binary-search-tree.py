# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        que = [[root, float("-inf"), float("inf")]] # node, max, min

        while que:
            [node, minval, maxval] = que.pop()
            if not (minval < node.val < maxval):
                return False
            if node.left:
                if node.val <= node.left.val:
                    return False
                else:
                    que.append([node.left, minval, node.val])
            if node.right:
                if node.val > node.right.val:
                    return False
                else:
                    que.append([node.right, node.val, maxval])
        
        return True
            
                    