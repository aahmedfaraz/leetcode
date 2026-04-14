class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        newStart, newEnd = newInterval
        i = 0
        n = len(intervals)

        # add all intervals before newInterval
        while i < n and intervals[i][1] < newStart:
            res.append(intervals[i])
            i += 1

        # merge overlapping intervals
        while i < n and intervals[i][0] <= newEnd:
            newStart = min(newStart, intervals[i][0])
            newEnd = max(newEnd, intervals[i][1])
            i += 1

        res.append([newStart, newEnd])

        # add remaining intervals
        while i < n:
            res.append(intervals[i])
            i += 1

        return res