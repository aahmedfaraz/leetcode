from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        data = {}
        maxval = 0
        res = []

        que = deque([root])
        while que:
            node = que.pop()

            if node.val in data:
                data[node.val] += 1
            else:
                data[node.val] = 1

            count = data[node.val]
            
            if count == maxval:
                res.append(node.val)
            elif count > maxval:
                maxval = count
                res = [node.val]
            
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)

        return res
