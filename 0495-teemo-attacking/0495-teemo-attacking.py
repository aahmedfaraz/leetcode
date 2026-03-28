class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if duration == 0: return 0

        poisoned = 0

        for i in range(len(timeSeries)-1):
            t1 = timeSeries[i]
            t2 = timeSeries[i+1]
            diff = t2 - t1
            poisoned += min(diff, duration)
        
        poisoned += duration        
        return poisoned