# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return None

        slow, fast = head, head.next

        while slow and fast and fast.next:
            if id(slow) == id(fast):
                break
            slow = slow.next
            fast = fast.next.next
        
        if id(slow) != id(fast): return None
        
        fast = fast.next

        curr = head
        while curr and fast and id(fast) != id(curr):
            curr = curr.next
            fast = fast.next
        
        return curr