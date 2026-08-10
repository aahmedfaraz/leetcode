# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def last_to_second(node):
            if not node or not node.next:
                return
            secondlastnode = None
            lastnode = node
            while lastnode.next: # O(n)
                secondlastnode = lastnode
                lastnode = lastnode.next
            second = node.next
            if second == lastnode:
                return
            node.next = lastnode
            lastnode.next = second
            secondlastnode.next = None
            last_to_second(second)
        last_to_second(head)
# Time = O(n^2)
# Space = O(n)