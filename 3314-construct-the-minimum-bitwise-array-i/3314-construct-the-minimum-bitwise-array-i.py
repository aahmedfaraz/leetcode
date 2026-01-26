class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for p in nums: # loop through all prime numbers
            found = -1 # if no num match

            # Find minimum number whose (i OR i+1) is p, so, loop from 0 -> p-1
            for i in range(p):
                if (i | (i+1)) == p:
                    found = i
                    break

            ans.append(found)

        return ans

# Time Complexity: O(n * m) where n is the length of nums and m is the maximum value in nums
# Space Complexity: O(1) ignoring the output array, ouput array is O(n)