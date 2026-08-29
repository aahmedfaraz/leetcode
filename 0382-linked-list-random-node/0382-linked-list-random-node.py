import random
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        
    def getRandom(self) -> int:
        curr = self.head
        reservoir = curr
        count = 0
        while curr:
            count += 1
            if random.randint(1, count) == 1:
                reservoir = curr
            curr = curr.next
        return reservoir.val