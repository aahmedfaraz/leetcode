class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        for h in range(12):
            for m in range(60):
                if (bin(h).count('1') + bin(m).count('1')) == turnedOn:
                    result.append(f"{h}:{m:02d}")
        return result

# time complexity = O(h x m) = O(12 x 60) = O(1)
# space complexity = O(h x m) = O(12 x 60) = O(1)