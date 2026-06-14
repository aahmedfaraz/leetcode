class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1)-1, len(num2)-1
        carry = 0
        ans = ""

        nums = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
        }

        while i >= 0 or j >= 0:
            if i >= 0 and j >= 0:
                localans = str(nums[num1[i]] + nums[num2[j]] + carry)
                if len(localans) == 1:
                    ans += localans
                    carry = 0
                else:
                    ans += localans[1]
                    carry = nums[localans[0]]
            else:
                if i < 0:
                    la = str(nums[num2[j]] + carry)
                    if len(la) > 1:
                        ans += la[1]
                        carry = nums[la[0]]
                    else:
                        ans += la
                        carry = 0
                if j < 0:
                    la = str(nums[num1[i]] + carry)
                    if len(la) > 1:
                        ans += la[1]
                        carry = nums[la[0]]
                    else:
                        ans += la
                        carry = 0
            i -= 1
            j -= 1

        if carry > 0:
            ans += str(carry)

        return ans[::-1]
