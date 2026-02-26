# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        lastPairlastNode = dummy
        currPairFirstNode = head

        while currPairFirstNode and currPairFirstNode.next:
            # get pointers
            currPairSecondNode = currPairFirstNode.next
            nextPairFirstNode = currPairFirstNode.next.next

            # swap
            currPairSecondNode.next = currPairFirstNode
            currPairFirstNode.next = nextPairFirstNode
            lastPairlastNode.next = currPairSecondNode

            # update pointers
            lastPairlastNode = currPairFirstNode
            currPairFirstNode = currPairFirstNode.next
        
        return dummy.next