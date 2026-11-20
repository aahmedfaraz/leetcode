class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        if (nums.size() == 1) return 1;

        int count = 0;
        int need = 0; // 0 = no need, 1 = need big, -1 = need small

        // check each element with next
        for (int i = 0; i < nums.size() - 1; i++) {
            // if elements are same, skip
            if (nums[i] == nums[i+1]) continue;
            
            // if need is not defined OR correct big found OR correct small found, increment
            if (
                need == 0 ||
                need > 0 && nums[i+1] > nums[i] ||
                need < 0 && nums[i+1] < nums[i]
            ) {
                count++;
                // set the next need
                need = (nums[i+1] < nums[i]) ? 1: -1;
            }
        }
        
        // last one is not added
        count++;

        return count;
    }
};