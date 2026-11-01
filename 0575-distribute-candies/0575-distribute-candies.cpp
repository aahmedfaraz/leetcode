class Solution {
public:
    int distributeCandies(vector<int>& candyType) {
        set<int> s(candyType.begin(), candyType.end()); // O(n log n)
        int half = candyType.size() / 2;
        int unique = s.size();
        if (half > unique) {
            return unique;
        } else {
            return half;
        }
    }
};

// Time = O(n log n)
// Space = O(n), we used another data structure set