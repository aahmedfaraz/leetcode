class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        data = { nums2[i]: i for i in range(len(nums2)) }
        for i in range(len(nums1)):
            num = nums1[i]
            nums1[i] = -1
            for j in range(data[num]+1, len(nums2)):
                if nums2[j] > num:
                    nums1[i] = nums2[j]
                    break
        return nums1
# Let, m = length of nums1, n = length of nums2
# Time = O(m x n)
# Space = O(n) hashmap