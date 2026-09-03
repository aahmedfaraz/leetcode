class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        # find all next smalls elements
        nextsm, mono = [-1] * n, []
        for i in range(n-1, -1, -1):
            height = heights[i]
            while mono and mono[-1][0] >= height:
                mono.pop()
            nextsm[i] = mono[-1][1] if mono else -1
            mono.append((height, i))

        # find all prev small elements
        prevsm, mono = [-1] * n, []
        for i in range(n):
            height = heights[i]
            while mono and mono[-1][0] >= height:
                mono.pop()
            prevsm[i] = mono[-1][1] if mono else -1
            mono.append((height, i))

        # find max rectangles from all heights
        maxarea = 0
        for i in range(n):
            height = heights[i]
            width = (n if nextsm[i] == -1 else nextsm[i]) - prevsm[i] - 1
            area = height * width
            maxarea = max(maxarea, area)
        
        return maxarea