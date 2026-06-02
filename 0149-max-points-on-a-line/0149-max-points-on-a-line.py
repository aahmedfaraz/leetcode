class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 2: return n
        maxpoints = 1
        for i in range(n-1):
            point1 = points[i]
            x1, y1 = point1[0], point1[1]
            slopes = {}
            # print("point1", point1)
            for j in range(i+1, n):
                point2 = points[j]
                x2, y2 = point2[0], point2[1]
                slope = float('inf')
                if x1 != x2:
                    slope = (y2-y1) / (x2-x1)
                if slope in slopes:
                    slopes[slope] += 1
                else:
                    slopes[slope] = 2
                maxpoints = max(maxpoints, slopes[slope])
                # print("-> point2", point2, " slopes ", slopes)
            
        return maxpoints