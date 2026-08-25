class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        data, n = [(nums[i], i) for i in range(len(nums))], len(nums)
        data.sort(key=lambda p: p[0])
        count = 0
        newdata = []
        newmap = {}
        for val in data:
            num, i = val
            if num in newmap:
                newdata.append((i, newmap[num]))
            else:    
                newdata.append((i, count))
                newmap[num] = count
            count += 1
        newdata.sort(key=lambda p: p[0])
        return [val[1] for val in newdata]