class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0: return []
        intervals = sorted(intervals, key=lambda x: x[0])

        groups = []
        prev = intervals[0]
        for i in range(1, len(intervals)):
            [start, end] = intervals[i]
            if prev[1] >= start:
                if prev[1] < end:
                    prev[1] = end
            else:
                groups.append(prev)
                prev = [start, end]
        groups.append(prev)
        return groups