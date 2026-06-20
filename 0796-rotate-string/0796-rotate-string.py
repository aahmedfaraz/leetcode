class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        if n != len(goal):
            return False
        if (s == "" and goal == "") or s == goal:
            return True

        # creating a circular linked list for string
        nodemap = {}
        start = Node('dummy')
        prev = start
        for ch in s:
            node = Node(ch)
            prev.next = node
            prev = node
            if ch in nodemap:
                nodemap[ch].append(node)
            else:
                nodemap[ch] = [node]
        prev.next = start.next # removed start/dummy-node automatically

        startCh = goal[0]
        if startCh not in nodemap:
            return False
        for node in nodemap[startCh]:
            i = 0
            matched = 0
            checked = 0
            while checked < n or matched < n:
                if goal[i] == node.val:
                    matched += 1
                else:
                    break
                checked += 1
                node = node.next
                if i+1 == n:
                    i = 0
                else:
                    i += 1
            if matched == n:
                return True
            i = 0

        return False


