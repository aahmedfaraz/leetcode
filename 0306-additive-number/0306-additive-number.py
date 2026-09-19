class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        if n < 3:
            return False

        def dfs(num1, num2, res, start):
            if (num1 + num2) != res:
                return False
            if start == n:
                return True
            if (num1 + num2) == res:
                for i in range(start+1, n+1):
                    if num[start] == '0' and (i-start) > 1:
                        break
                    newres = int(num[start:i])
                    if dfs(num2, res, newres, i):
                        return True
            return False
            
        for i in range(1, (n+1) // 2):
            if num[0] == '0' and i > 1:
                break
            num1 = int(num[0:i])
            for j in range(i+1, n):
                if num[i] == '0' and (j-i) > 1:
                    break
                num2 = int(num[i:j])
                for k in range(j+1, n+1):
                    if num[j] == '0' and (k-j) > 1:
                        break
                    res = int(num[j:k])
                    if dfs(num1, num2, res, k):
                        return True

        return False