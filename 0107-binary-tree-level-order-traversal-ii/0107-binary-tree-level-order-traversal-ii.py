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
            currLevelVals = []
            for node in level:
                if node:
                    currLevelVals.append(node.val)
                    if node.left:
                        nextLevel.append(node.left)
                    if node.right:
                        nextLevel.append(node.right)
            res.append(currLevelVals)
            level = nextLevel
        return res[::-1]