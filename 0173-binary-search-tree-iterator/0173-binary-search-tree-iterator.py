class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []

        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stack.pop()

        cur = node.right
        while cur:
            self.stack.append(cur)
            cur = cur.left

        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0