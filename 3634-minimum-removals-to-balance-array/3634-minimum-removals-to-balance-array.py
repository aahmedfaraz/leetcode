class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1: return 0

        # timsort
        nums.sort() # O(n log n)

        # two-pointer, find largest list with balanced elements
        bal_len = 0 # size of largest balanced list
        left, right = 0, 0

        while right < n:
            MIN = nums[left]
            MAX = nums[right]

            if MAX <= (MIN * k):
                new_bal_len = right - left + 1
                bal_len = max(bal_len, new_bal_len)
                right += 1
            else:
                left += 1

        # total deletions = original list size - size of largest balanced list
        return n - bal_len

# Time complexity
# - timsort : O(n log n)
# - while loop : O(n)
# Overall time complexity = O(n log n) + O(n) = O(n log n)

# Space complexity
# O(1) - we are only saving pointers and size of largest balanced list