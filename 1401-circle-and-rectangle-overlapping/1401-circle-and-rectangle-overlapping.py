class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        nearestx, nearesty = float('inf'), float('inf')

        if x1 <= xCenter <= x2:
            nearestx = xCenter
        elif xCenter <= x1:
            nearestx = x1
        elif x2 <= xCenter:
            nearestx = x2

        if y1 <= yCenter <= y2:
            nearesty = yCenter
        elif yCenter <= y1:
            nearesty = y1
        elif y2 <= yCenter:
            nearesty = y2
        
        dist = abs((xCenter-nearestx))**2 + abs((yCenter-nearesty))**2
        
        return (radius*radius) >= dist