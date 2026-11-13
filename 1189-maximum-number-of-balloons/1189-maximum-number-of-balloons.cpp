class Solution {
public:
    int maxNumberOfBalloons(string text) {
        unordered_map<char, int> counter;
        for (char c: text) {
            counter[c] += 1;
        }
        for (auto item: counter) {
            cout << item.first << " : " << item.second << endl;
        }
        return min({counter['b'], counter['a'], counter['n'], counter['l'] / 2, counter['o'] / 2});
    }
};