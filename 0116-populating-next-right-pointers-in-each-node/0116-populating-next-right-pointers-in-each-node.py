"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None

        level = [root]
        
        while level:
            newlevel = []
            for i in range(len(level)):
                node = level[i]
                if node:
                    newlevel.extend([node.left, node.right])
                    if i == len(level)-1:
                        node.next = None
                    else:
                        node.next = level[i+1]
            level = newlevel
        return root