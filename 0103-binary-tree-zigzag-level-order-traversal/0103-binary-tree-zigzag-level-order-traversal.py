# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        curr_level = [root]
        next_level = []
        all_levels = []
        level = 0

        while curr_level:
            curr_vals = []

            for node in curr_level:
                curr_vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            if level%2 == 1:
                curr_vals.reverse()

            all_levels.append(curr_vals)
            curr_level = next_level.copy()
            next_level = []
            level += 1
        
        return all_levels
