#include <string>
class Solution {
public:
    string truncateSentence(string s, int k) {
        int spaces = 0;
        int end = s.size();
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == ' ') {
                spaces += 1;
            }
            if (spaces == k) {
                end = i;
                break;
            }
        }
        return s.substr(0, end);
    }
};