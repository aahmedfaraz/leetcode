class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        pairs = [[nums1[0] + nums2[0], 0, 0]]
        ans = []
        test = set()

        while pairs and k:
            _, a, b = heapq.heappop(pairs)
            ans.append([nums1[a], nums2[b]])
            if a < (m-1) and not (a+1, b) in test:
                heapq.heappush(pairs, [nums1[a+1] + nums2[b], a+1, b])
            if b < (n-1) and not (a, b+1) in test:
                heapq.heappush(pairs, [nums1[a] + nums2[b+1], a, b+1])
            # print('For', a, b, 'added', a+1, b, 'and', a, b+1, '- Duplication:', (a+1, b) in test or (a, b+1) in test)
            test.add((a+1, b))
            test.add((a, b+1))

            k -= 1
        
        return ans