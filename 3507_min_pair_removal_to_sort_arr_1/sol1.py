class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        # Function to check if list is in increasing order or not
        def incOrder(nums: List[int]) -> bool:
            for i in range(len(nums) - 1): # O(n)
                if nums[i] > nums[i+1]:
                    return False
            return True
        
        operations = 0
        while not incOrder(nums): #O(n)
            # create pair sums, for n nums it will create n-1 sums
            sums = [nums[i] + nums[i+1] for i in range(len(nums) - 1)] # O(n)
            
            # Get the min sum pair
            min_sum = min(sums) # O(n)
            min_sum_index = sums.index(min_sum) # O(n)
            min_sum_pair_index = [min_sum_index, min_sum_index+1]
            
            # Replace the pair with their sum, place the sum on left side and remove the right num of pair
            nums[min_sum_pair_index[0]] = nums[min_sum_pair_index[0]] + nums[min_sum_pair_index[1]]
            del nums[min_sum_pair_index[1]] # O(n)

            operations += 1

        return operations


# Example usage (from LeetCode problem):
print(Solution().minimumPairRemoval([5, 2, 3, 1]))  # Example 1
print(Solution().minimumPairRemoval([1, 2, 2]))     # Example 2

# Time Complexity:
# Let n be the length of nums.
# The check for non-decreasing order is O(n).
# Inside the while loop per operation:
# - building sums: O(n)
# - finding min and its index: O(n)
# - deleting an element: O(n)
# In the worst case, the loop runs O(n) times → O(n^2) overall.

# Space Complexity:
# O(n) for the sums list in each iteration.

# OUTPUT:
# 2
# 0
