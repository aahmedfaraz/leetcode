# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        mapt = {}

        def bst(start, end):
            if start > end:
                return [None]

            if (start, end) in mapt:
                return mapt[(start, end)]
            
            trees = []

            for rootval in range(start, end+1):
                leftTrees = bst(start, rootval-1)
                rightTrees = bst(rootval+1, end)

                for leftT in leftTrees:
                    for rightT in rightTrees:
                        root = TreeNode(rootval, leftT, rightT)
                        trees.append(root)
            
            mapt[(start, end)] = trees
            if start == end:
                print(trees)
            return trees

        return bst(1, n)