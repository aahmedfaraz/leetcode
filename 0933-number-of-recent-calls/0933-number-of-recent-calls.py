class Node:
    def __init__(self, t, next=None):
        self.t = t
        self.next = next

class RecentCounter:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def ping(self, t: int) -> int:
        newcall = Node(t)
        if not self.head:
            self.head = newcall
            self.tail = newcall
            self.size = 1
        else:
            self.tail.next = newcall
            self.tail = newcall
            self.size += 1
        start = t - 3000
        while self.head and self.head.t < start:
            oldnode = self.head
            self.head = self.head.next
            del oldnode
            self.size -= 1
        if not self.head:
            self.tail = None
        return self.size


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)