from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        result = []
        for x in nums:
            # If x == 2, no valid a exists
            if x == 2:
                result.append(-1)
                continue

            # Find the first 0 bit from the right (starting at position 1)
            ans = -1
            for i in range(1, 32):
                if ((x >> i) & 1) == 0:
                    # Flip the bit at (i - 1) to get minimum a
                    ans = x ^ (1 << (i - 1))
                    break

            result.append(ans)
        return result


# -----------------------------
# Example usage (LeetCode 3315)
# -----------------------------

sol = Solution()

print(sol.minBitwiseArray([2, 3, 4]))
# Expected Output: [-1, 1, 2]

print(sol.minBitwiseArray([1, 5, 7]))
# Expected Output: [0, 4, 5]

print(sol.minBitwiseArray([2]))
# Expected Output: [-1]


# -----------------------------
# Time Complexity:
# -----------------------------
# Let n be the length of nums.
# For each number, we scan up to 31 bits.
# Time Complexity: O(n * 32) ≈ O(n)

# -----------------------------
# Space Complexity:
# -----------------------------
# Output array stores n elements.
# Space Complexity: O(n)