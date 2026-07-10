class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m, n = len(nums1), len(nums2)
        stack = []
        data = {}
        for i in range(n): # O(n)
            num = nums2[i]
            while stack and stack[-1] < num: # O(k), k <= n
                data[stack.pop()] = num # O(1)
            stack.append(num) # amortized O(1)
        for num in stack: # O(k)
            data[num] = -1
        for i in range(m): # O(m)
            nums1[i] = data[nums1[i]]
        return nums1
# Time = O(n) + O(k) + O(m)
# = O(n) + O(n) + O(m)
# = O(2n) + O(m)
# = O(n + m)

# Space = O(n) stack space