class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointer technique, O(n)
        left, right = 0, len(height)-1
        max_area = 0
        while left < right:
            container_length = right - left
            container_height = min(height[left], height[right])
            area = container_length * container_height
            max_area = max(max_area, area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_area


        # # brute force, O(n^2)
        # max_area = 0
        # for i in range(len(height)):
        #     for j in range(i, len(height)):
        #         l = j - i
        #         h = min(height[i], height[j])
        #         area = l * h
        #         if area > max_area: max_area = area
        # return max_area