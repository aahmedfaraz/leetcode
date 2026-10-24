class Solution {
public:
    string sum(string subs) {
        int sum = 0;
        int i = 0;
        while (i < subs.size()) {
            sum += (subs[i] - '0');
            i += 1;
        }
        return std::to_string(sum);
    }

    string digitSum(string s, int k) {
        while (s.size() > k) {
            int i = 0;
            string news = "";
            
            while (i < s.size()) {
                news += sum(s.substr(i, k));
                i += k;
            }
            s = news;
        }

        return s;
    }
};