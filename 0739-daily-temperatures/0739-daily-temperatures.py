class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        res = [0] * n

        stack = []  # stores indices

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_i = stack.pop()
                res[prev_i] = i - prev_i

            stack.append(i)

        return res