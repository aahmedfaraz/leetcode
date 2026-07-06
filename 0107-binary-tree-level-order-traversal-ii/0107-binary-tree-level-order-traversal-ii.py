# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        level = [root]
        res = []
        
        while level:
            nextLevel = []
            nextLevelHasANode = False
            currLevelVals = []
            for node in level:
                if node:
                    currLevelVals.append(node.val)
                    nextLevel.append(node.left)
                    nextLevel.append(node.right)
                    if node.left or node.right:
                        nextLevelHasANode = True
            res.append(currLevelVals)
            if not nextLevelHasANode:
                level = []
            else:
                level = nextLevel
        return res[::-1]