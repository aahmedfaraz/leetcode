import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        if m == 0 and n == 0: return 0
        elif m == 0 and n == 1: return nums2[0]
        elif m == 1 and n == 0: return nums1[0]

        total = m + n
        i, j = 0, 0
        if total % 2 == 0:
            j = total // 2
            i = j - 1
        else:
            i = total // 2
            j = i
        
        k, l = 0, 0
        med_num1 = float('inf')
        med_num2 = float('inf')

        merged_index = 0

        while k < m or l < n:
            if k < m and (l >= n or nums1[k] <= nums2[l]):
                current = nums1[k]
                k += 1
            else:
                current = nums2[l]
                l += 1

            if merged_index == i:
                med_num1 = current
            if merged_index == j:
                med_num2 = current

            merged_index += 1

            if merged_index > j:
                break

        print(med_num1, med_num2)

        if total % 2 == 0:
            return (med_num1 + med_num2) / 2
        else:
            return med_num1
