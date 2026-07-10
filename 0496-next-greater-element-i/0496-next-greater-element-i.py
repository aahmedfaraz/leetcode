class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m, n = len(nums1), len(nums2)
        stack = []
        data = {}
        for i in range(n):
            num = nums2[i]
            while stack and stack[-1] < num:
                data[stack.pop()] = num
            stack.append(num)
        for num in stack:
            data[num] = -1
        for i in range(m):
            nums1[i] = data[nums1[i]]
        return nums1