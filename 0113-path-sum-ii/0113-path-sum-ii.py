from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        if not root:
            return []
        que = deque([(root, 0, [])])

        while que:
            node, summ, seq = que.popleft()
            summ += node.val
            seq.append(node.val)
            if not node.left and not node.right:
                if summ == targetSum:
                    res.append(seq.copy())
            else:
                if node.left:
                    que.append((node.left, summ, seq.copy()))
                if node.right:
                    que.append((node.right, summ, seq.copy()))
        return res

# Time = O(n)
# Space = O(n)
