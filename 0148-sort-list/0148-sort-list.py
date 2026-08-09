# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        def mergesort(head):
            if not head or not head.next:
                return head
            
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            mid = slow
            left, right = head, mid.next
            mid.next = None
            
            leftsorted = mergesort(left)
            rightsorted = mergesort(right)

            return merge(leftsorted, rightsorted)

        def merge(head1, head2):
            dummy = ListNode(0)
            res = dummy

            while head1 and head2:
                if head1.val <= head2.val:
                    res.next = head1
                    head1 = head1.next
                else:
                    res.next = head2
                    head2 = head2.next
                res = res.next
            
            if head1:
                res.next = head1
            else:
                res.next = head2
            
            return dummy.next
        
        return mergesort(head)