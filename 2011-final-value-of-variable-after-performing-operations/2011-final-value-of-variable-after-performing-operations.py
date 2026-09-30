class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        val = 0

        for op in operations:
            if '-' in op:
                val -= 1
            else:
                val += 1
        
        return val