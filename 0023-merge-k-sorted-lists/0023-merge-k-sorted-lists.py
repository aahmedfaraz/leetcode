# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        res = ListNode()
        curr = res

        countNull = 0

        while countNull < n:
            # print('count', countNull)
            countNull = 0
            minValNode = ListNode(float('inf'))
            ind = -1
            for i, node in enumerate(lists):
                if node != None:
                    if node.val < minValNode.val:
                        minValNode = node
                        ind = i
                else:
                    countNull += 1
            if ind >= 0:
                # print(ind, curr.val, minValNode.val)
                curr.next = minValNode
                curr = curr.next
                lists[ind] = lists[ind].next

        return res.next

# Time complexity = O(n), we are accessing all nodes by once
# Space complexity = O(1), no extra space is used other than output