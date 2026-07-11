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
        while que: # O(n)
            node = que.pop() # O(1)

            if node.val in data:
                data[node.val] += 1 # O(1)
            else:
                data[node.val] = 1 # O(1)

            count = data[node.val] # O(1)
            
            if count == maxval:
                res.append(node.val) # O(1)
            elif count > maxval:
                maxval = count
                res = [node.val] # O(1)
            
            if node.left:
                que.append(node.left) # O(1)
            if node.right:
                que.append(node.right) # O(1)

        return res

# Time = O(n)
# Space = O(n)