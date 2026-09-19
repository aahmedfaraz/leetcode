class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        n = len(num)
        if n == 1:
            return [num]

        combs = []

        def calculate(comb):
            nums = []
            ops = []
            m = len(comb)
            sign = 1

            i = 0

            while i < m:
                ch = comb[i]

                if ch.isdigit():
                    numstr = []
                    longernumber = False
                    numstr.append(ch)
                    
                    while i < (m-1) and comb[i+1].isdigit():
                        i += 1
                        ch = comb[i]
                        numstr.append(ch)

                    numint = int("".join(numstr)) * sign
                    sign = 1
                    
                    if ops and ops[-1] == '*':
                        prevnum = nums.pop()
                        thisnum = numint
                        nums.append(prevnum * thisnum)
                        ops.pop()
                    elif ops and ops[-1] == '-':
                        ops.pop()
                        ops.append('+')
                        nums.append(-numint)
                    else:
                        nums.append(numint)
                else:
                    if ch == '-':
                        if nums:
                            ops.append('+')
                        sign = -1
                    else:
                        ops.append(ch)

                i += 1

            while ops:
                num1 = nums.pop()
                num2 = nums.pop()
                op = ops.pop()
                if op == '+':
                    nums.append(num1+num2)
                else:
                    nums.append(num1-num2)           
            
            return nums[0]

        def dfs(path, idx):
            nonlocal combs
            # print(path, idx)

            if idx == n:
                if calculate(path) == target:
                    combs.append("".join(path))
                return

            for i in range(idx+1, n+1):
                if num[idx] == '0' and (i-idx) > 1:
                    break
                path.append('*')
                path.append(num[idx: i])
                dfs(path, i)
                path.pop()
                path.pop()

                path.append('+')
                path.append(num[idx: i])
                dfs(path, i)
                path.pop()
                path.pop()

                path.append('-')
                path.append(num[idx: i])
                dfs(path, i)
                path.pop()
                path.pop()

        for i in range(1, n+1):
            if num[0] == '0' and i > 1:
                break
            dfs([num[0:i]], i)
        
        return combs
