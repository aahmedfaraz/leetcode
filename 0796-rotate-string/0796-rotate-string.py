class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)

        if n != len(goal):
            return False

        if s == goal:
            return True

        # try every possible starting index in s
        for start in range(n):
            matched = True

            for i in range(n):
                if s[(start + i) % n] != goal[i]:
                    matched = False
                    break

            if matched:
                return True

        return False