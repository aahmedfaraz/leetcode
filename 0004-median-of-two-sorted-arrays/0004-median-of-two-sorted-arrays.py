import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        if m == 0 and n == 0: return 0
        elif m == 0 and n == 1: return nums2[0]
        elif m == 1 and n == 0: return nums1[0]

        total = m + n

        # calculate median positions
        i, j = 0, 0
        if total % 2 == 0:
            j = total // 2
            i = j - 1
        else:
            i = total // 2
            j = i
        
        # pointers for tracking
        k, l = 0, 0
        med_num1 = float('inf')
        med_num2 = float('inf')

        merged_index = 0  # index in virtual merged array

        while k < m or l < n:
            if k >= m: # nums1 array is finished, take element from nums2
                curr_selected_num = nums2[l]
                l += 1
            elif l >= n: # nums2 array is finished, take element from nums1
                curr_selected_num = nums1[k]
                k += 1
            elif nums1[k] <= nums2[l]: # both arrays have elements, pick smaller element
                curr_selected_num = nums1[k]
                k += 1
            else:
                curr_selected_num = nums2[l]
                l += 1

            # save median values when index matches
            if merged_index == i:
                med_num1 = curr_selected_num
            if merged_index == j:
                med_num2 = curr_selected_num

            merged_index += 1

            # medians are found, break
            if merged_index > j:
                break

        # calculate and return median
        if total % 2 == 0:
            return (med_num1 + med_num2) / 2
        else:
            return med_num1


# Time Complexity: O(m + n), reading all elements one time
# Space Complexity: O(1), used pointers and 2 variables to save medians