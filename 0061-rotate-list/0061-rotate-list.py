class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # make list a cycle and count nodes
        curr = head
        n = 1
        while curr.next:
            curr = curr.next
            n += 1
        curr.next = head  # make cycle

        # reduce k
        k %= n
        if k == 0:
            curr.next = None
            return head

        # move to new tail
        steps = n - k
        tail = head
        for _ in range(steps - 1):
            tail = tail.next

        newhead = tail.next

        # break the cycle
        tail.next = None

        return newhead