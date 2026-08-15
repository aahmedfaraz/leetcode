import random
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.nodes = {}
        idx = 0
        curr = head
        while curr:
            self.nodes[idx] = curr
            curr = curr.next
            idx += 1
        self.size = idx

    def getRandom(self) -> int:
        if self.size == 1:
            return self.nodes[0].val
        idx = random.randint(0, self.size-1)
        return self.nodes[idx].val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()