# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-5001, head)
        prev = dummy
        curr = dummy.next

        while curr:
            if prev.val > curr.val:
                prev.next = curr.next
                p = dummy
                node = dummy.next
                while node.val < curr.val:
                    p = node
                    node = node.next
                p.next = curr
                curr.next = node
            prev = curr
            curr = curr.next

        return dummy.next