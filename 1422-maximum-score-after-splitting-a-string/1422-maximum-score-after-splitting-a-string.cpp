
class Solution {
public:
    int maxScore(string s) {
        int zeros = 0;
        int ones = 0;
        int ans = 0;

        // Count all ones initially
        for (char c : s) {
            if (c == '1') {
                ones++;
            }
        }

        // Move characters from right to left,
        // keeping the right part non-empty
        for (int i = 0; i < s.size() - 1; i++) {
            if (s[i] == '0') {
                zeros++;
            } else {
                ones--;
            }

            ans = max(ans, zeros + ones);
        }

        return ans;
    }
};
