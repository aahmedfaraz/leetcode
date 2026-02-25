class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles # 12

        while numBottles >= numExchange: # 3 >= 3
            remainingEmpty = numBottles % numExchange # 0
            newFilled = numBottles // numExchange # 3
            total += newFilled # 12
            numBottles = newFilled + remainingEmpty # 3 + 0 = 3

        return total

# time complexity = O(n/e)
# space complexity = O(1)