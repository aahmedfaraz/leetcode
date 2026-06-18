# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        hero = []
        res = []
        if not root:
            return []
        def dfs(root, summ):
            nonlocal hero
            hero.append(root.val)
            summ += root.val
            if not root.left and not root.right:
                if summ == targetSum:
                    res.append(hero.copy())
            else:
                if root.left:
                    dfs(root.left, summ)
                if root.right:
                    dfs(root.right, summ)            
            summ -= root.val
            hero.pop()
        
        dfs(root, 0)

        return res

