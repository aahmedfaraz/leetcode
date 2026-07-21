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
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root

        layer = [root]

        def dfs(layer):
            if not layer: return
            newlayer = []
            for i in range(len(layer)):
                node = layer[i]
                if node.left:
                    newlayer.append(node.left)
                if node.right:
                    newlayer.append(node.right)
                node.next = layer[i+1] if i < len(layer)-1 else None
            dfs(newlayer)
        
        dfs(layer)
        
        return root
