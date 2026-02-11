import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)  # length of first array
        n = len(nums2)  # length of second array

        # Handle small edge cases
        if m == 0 and n == 0: return 0
        elif m == 0 and n == 1: return nums2[0]
        elif m == 1 and n == 0: return nums1[0]

        total = m + n  # total elements count

        # Find median index positions
        i, j = 0, 0
        if total % 2 == 0:
            j = total // 2      # right median index
            i = j - 1           # left median index
        else:
            i = total // 2      # single median index
            j = i
        
        # Pointers for nums1 and nums2
        k, l = 0, 0

        # Store median values
        med_num1 = float('inf')
        med_num2 = float('inf')

        merged_index = 0  # index in virtual merged array

        # Merge traversal until median positions reached
        while k < m or l < n:
            # Choose smaller current element
            if k < m and (l >= n or nums1[k] <= nums2[l]):
                current = nums1[k]
                k += 1
            else:
                current = nums2[l]
                l += 1

            # Capture median values when index matches
            if merged_index == i:
                med_num1 = current
            if merged_index == j:
                med_num2 = current

            merged_index += 1

            # Stop early once median found
            if merged_index > j:
                break

        # Return median based on total count parity
        if total % 2 == 0:
            return (med_num1 + med_num2) / 2
        else:
            return med_num1


# Time Complexity: O(m + n)  -> Merge traversal until median index
# Space Complexity: O(1)     -> No extra data structures used
