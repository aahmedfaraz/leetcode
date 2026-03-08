# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <= 1: return head

        dummy = ListNode(0, head)
        prevSeriesLastElement = dummy
        newSeriesFirstElement = dummy.next

        def checkRemaining(node, k):
            count = 0
            valid = True
            while node and count < k:
                count += 1
                node = node.next
            return count == k
            

        while checkRemaining(newSeriesFirstElement, k):
            count = 0
            curr1 = newSeriesFirstElement
            curr2 = newSeriesFirstElement.next
            while count < (k-1):
                curr3 = curr2.next if curr2 else None
                count += 1
                curr2.next = curr1
                curr1 = curr2
                curr2 = curr3
            prevSeriesLastElement.next = curr1
            newSeriesFirstElement.next = curr2

            prevSeriesLastElement = newSeriesFirstElement
            newSeriesFirstElement = curr2
        
        return dummy.next
                
            

        return dummt.next