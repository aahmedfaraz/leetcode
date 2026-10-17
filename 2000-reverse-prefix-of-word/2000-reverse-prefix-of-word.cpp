class Solution {
public:
    string reversePrefix(string word, char ch) {
        int i = 0;
        while (i < word.size() && word[i] != ch) {
            i += 1;
        }
        if (i == word.size())
            return word;
        int j = 0;
        while (i > j) {
            char temp = word[i];
            word[i] = word[j];
            word[j] = temp;
            j += 1;
            i -= 1;
        }
        return word;
    }
};