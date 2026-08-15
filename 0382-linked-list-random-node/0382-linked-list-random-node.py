import random
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        self.size = count

    def getRandom(self) -> int:
        if not self.head.next:
            return self.head.val
        target = random.randint(1, self.size)
        curr = self.head
        count = 1
        while count < target:
            count += 1
            curr = curr.next
        return curr.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()