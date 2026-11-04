
class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {

        if (numerator == 0) return "0";

        string ans = "";

        // Handle negative sign
        if ((numerator < 0) != (denominator < 0)) {
            ans += "-";
        }

        // Convert to long long to avoid INT_MIN overflow
        long long n = abs((long long)numerator);
        long long d = abs((long long)denominator);

        // Integer part
        ans += to_string(n / d);

        long long remainder = n % d;

        if (remainder == 0) return ans;

        ans += ".";

        unordered_map<long long, int> seen;

        while (remainder != 0) {

            // Check if remainder has appeared before
            if (seen.find(remainder) != seen.end()) {

                int pos = seen[remainder];

                ans.insert(pos, "(");
                ans += ")";

                break;
            }

            // Store remainder and its position
            seen[remainder] = ans.size();

            // Calculate next decimal digit
            remainder *= 10;

            ans += to_string(remainder / d);

            remainder %= d;
        }

        return ans;
    }
};
