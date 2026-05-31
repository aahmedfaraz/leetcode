class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # count each num in nums1
        counter_nums1 = {}
        for num in nums1:
            if num in counter_nums1:
                counter_nums1[num] += 1
            else:
                counter_nums1[num] = 1
        
        # check if we have those elements in nums2 add them in res
        res = []
        for num in nums2:
            if num in counter_nums1 and counter_nums1[num] > 0:
                counter_nums1[num] -= 1
                res.append(num)
        
        return res