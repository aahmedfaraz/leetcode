# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(float('-inf'))

        # attach all small ones
        curr = head
        dcurr = dummy
        while curr:
            if curr.val < x:
                dcurr.next = ListNode(curr.val)
                dcurr = dcurr.next
            curr = curr.next

        # attach remaining large ones
        curr = head
        while curr:
            if curr.val >= x:
                dcurr.next = ListNode(curr.val)
                dcurr = dcurr.next
            curr = curr.next
        
        return dummy.next