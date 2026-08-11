# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return head

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        l2 = slow.next
        slow.next = None
        prev = None
        while l2:
            nextnode = l2.next
            l2.next = prev
            prev = l2
            l2 = nextnode

        part1 = head
        part2 = prev

        curr1 = head
        curr2 = part2

        while curr1 and curr2:
            second = curr1.next
            secondlast = curr2.next
            
            curr1.next = curr2
            curr2.next = second

            curr1 = second
            curr2 = secondlast

# head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

# Solution.reorderlist(head)