class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float('inf')
        min_arr = []
        for i in range(len(arr) - 1):
            diff = arr[i+1] - arr[i]
            if diff < min_diff:
                min_diff = diff
                min_arr = [[arr[i], arr[i+1]]]
            elif diff == min_diff:
                min_arr.append([arr[i], arr[i+1]])
        return min_arr
        