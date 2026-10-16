using namespace std;

class Solution {
public:
    int maxScore(string s) {
        int sum = 0;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == '1') {
                sum += 1;
            }
        }
        int score = 0;
        int zeros = 0;
        int ones = 0;
        for (int i = 0; i < s.size()-1; ++i) {
            if (s[i] == '0') {
                zeros += 1;
            } else {
                ones += 1;
            }
            int currscore = zeros + (sum - ones);
            if (currscore > score) {
                score = currscore;
            }
        }
        return score;
    }
};