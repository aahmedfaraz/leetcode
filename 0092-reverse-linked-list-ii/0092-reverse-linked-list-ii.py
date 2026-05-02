class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prevLeft = dummy

        # 1. Move prevLeft to node before "left"
        for _ in range(left - 1):
            prevLeft = prevLeft.next

        # 2. Start reversing
        curr = prevLeft.next
        prev = None

        for _ in range(right - left + 1):
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        # 3. Reconnect
        prevLeft.next.next = curr  # tail connects to remaining list
        prevLeft.next = prev       # head of reversed part

        return dummy.next