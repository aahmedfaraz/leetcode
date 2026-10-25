class Solution {
public:
    string removeOuterParentheses(string s) {
        string res = "";
        int counto = 0;
        for (char ch: s) {
            if (ch == '(') {
                counto += 1;
                if (counto > 1) {
                    res += ch;
                }
            } else {
                counto -= 1;
                if (counto > 0) {
                    res += ch;
                }
            }
        }
        return res;
    }
};