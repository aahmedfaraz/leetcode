class Solution {
public:
    int maximumGap(vector<int>& nums) {
        int n = nums.size();

        if (n <= 1) {
            return 0;
        }

        sort(nums.begin(), nums.end());

        int prev = nums[0];
        int max = 0;

        for (int num: nums) max = std::max(max, num - prev), prev = num;

        return max;
    }
};