from collections import deque

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque(tickets)
        seconds = 0

        while queue:
            if queue[0] > 1:
                queue.append(queue.popleft()-1)
                k -= 1
            else:
                queue.popleft()
                if k == 0:
                    seconds += 1
                    break
                k -= 1
            if k == -1:
                k = len(queue)-1
            seconds += 1
        
        return seconds