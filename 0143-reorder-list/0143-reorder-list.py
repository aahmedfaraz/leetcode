# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return head

        # find mid of the list - O(n)
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the other half of the list - O(n)
        l2 = slow.next
        slow.next = None
        prev = None
        while l2:
            nextnode = l2.next
            l2.next = prev
            prev = l2
            l2 = nextnode

        # merge the lists in required way - O(n)
        curr1 = head
        curr2 = prev
        while curr1 and curr2:
            second = curr1.next
            secondlast = curr2.next
            
            curr1.next = curr2
            curr2.next = second

            curr1 = second
            curr2 = secondlast

# Time = O(n)
# Space = O(1)