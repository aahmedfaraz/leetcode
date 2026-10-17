class Solution {
public:
    int numPrimeArrangements(int n) {
        const long long MOD = 1'000'000'007;

        int primecount = 0;

        for (int num=2; num <= n; num++) {
            bool isprime = true;

            for (int i = 2; i <= num/2; i++) {
                if (num % i == 0) {
                    isprime = false;
                    break;
                }
            }

            if (isprime) {
                primecount++;
            }
        }

        long long ans = 1;

        for (int i = primecount; i > 1; i--) {
            ans = (ans * i) % MOD;
        }

        for (int i = (n-primecount); i > 1; i--) {
            ans = (ans * i) % MOD;
        }

        return ans % MOD;
    }
};