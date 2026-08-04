class Solution:
    def checkRecord(self, s: str) -> bool:
        late = 0
        absent = 0
        for att in s:
            if att == 'A':
                absent += 1
                late = 0
                if absent >= 2:
                    return False
            elif att == 'L':
                late += 1
                if late >= 3:
                    return False
            else:
                late = 0
        return True