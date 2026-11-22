class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = parent[:]           # final parent after changes
        last = [[] for _ in range(26)]   # stack of open ancestors per letter
        order = []                       # preorder of the original tree

        stack = [0]
        while stack:
            u = stack.pop()
            if u >= 0:                   # entering u
                c = ord(s[u]) - 97
                if last[c]:
                    new_parent[u] = last[c][-1]   # closest same-char ancestor
                last[c].append(u)
                order.append(u)
                stack.append(~u)         # marker to exit u later
                stack.extend(children[u])
            else:                        # exiting u
                u = ~u
                last[ord(s[u]) - 97].pop()

        size = [1] * n
        for u in reversed(order):        # children are processed before ancestors
            if u:
                size[new_parent[u]] += size[u]
        return size