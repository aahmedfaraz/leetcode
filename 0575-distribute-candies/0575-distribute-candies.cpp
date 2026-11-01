#include <algorithm>

class Solution {
public:
    int distributeCandies(vector<int>& candyType) {
        set<int> s(candyType.begin(), candyType.end());
        int half = candyType.size() / 2;
        int unique = s.size();
        return min(half, unique);
    }
};