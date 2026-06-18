class Solution:
    def pathSum(self, root, targetSum):
        if not root:
            return []

        hero = []
        res = []

        def dfs(node, summ):
            hero.append(node.val)
            summ += node.val

            if not node.left and not node.right:
                if summ == targetSum:
                    res.append(hero.copy())
            else:
                if node.left:
                    dfs(node.left, summ)
                if node.right:
                    dfs(node.right, summ)

            hero.pop()

        dfs(root, 0)
        return res

# Time = O(n)
# Space = O(h)

# Where n is total nodes, and h is height of the tree