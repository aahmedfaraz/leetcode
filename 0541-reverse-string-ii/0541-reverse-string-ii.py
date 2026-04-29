class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        arr = list(s)

        for i in range(0, len(arr), 2 * k):
            left = i
            right = min(i + k - 1, len(arr) - 1)

            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        return ''.join(arr)