# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        current_level = [root]
        next_level = []
        levels = []

        while current_level:
            # add whole new level
            next_level_values = []

            for node in current_level:
                next_level_values.append(node.val)
                # fill next level
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            levels.append(next_level_values)
            current_level = next_level.copy()
            next_level = []
            
        return levels
