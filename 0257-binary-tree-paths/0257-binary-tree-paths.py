# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(prev, root):
            if not root: [prev]
            if not root.left and not root.right:
                return [f'{prev}{'->' if prev != "" else ""}{root.val}']
            combs = []
            if root.left:
                combs.extend(dfs(f'{prev}{'->' if prev != "" else ""}{root.val}', root.left))
            if root.right:
                combs.extend(dfs(f'{prev}{'->' if prev != "" else ""}{root.val}', root.right))
            return combs
        return dfs("", root)