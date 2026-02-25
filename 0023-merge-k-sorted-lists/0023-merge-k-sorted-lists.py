import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # fill heap will all nodes
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        res = ListNode()
        curr = res

        # take smallest elements from heap
        while heap:
            val, i, node = heapq.heappop(heap)

            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return res.next

# Time complexity = O(n log k), we are accessing all n nodes by once, finding min in O(log k)
# Space complexity = O(k), we are usin heap




        '''
        # Naiva approach

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

# Time complexity = O(n x k), we are accessing all n nodes by once, finding min in O(k)
# Space complexity = O(1), no extra space is used other than output
            '''