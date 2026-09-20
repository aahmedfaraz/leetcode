class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        nearestx = max(x1, min(xCenter, x2))
        nearesty = max(y1, min(yCenter, y2))
        return (radius*radius) >= (abs((xCenter-nearestx))**2 + abs((yCenter-nearesty))**2)