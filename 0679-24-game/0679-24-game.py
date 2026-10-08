class Solution:
    def judgePoint24(self, cards: list[int]) -> bool:
        def bt(rem):
            if len(rem) == 1:
                return abs(rem[0] - 24) < 1e-6
            
            ans = False

            for i in range(len(rem)):
                for j in range(len(rem)):
                    if i == j:
                        continue
                    num1 = rem[i]
                    num2 = rem[j]
                    newrem = []
                    for k in range(len(rem)):
                        if k == i or k == j:
                            continue
                        newrem.append(rem[k])

                    ans = ans or bt(newrem + [num1+num2])
                    if ans:
                        break
                    ans = ans or bt(newrem + [num1-num2])
                    if ans:
                        break
                    ans = ans or bt(newrem + [num1*num2])
                    if ans:
                        break
                    if num2 != 0:
                        ans = ans or bt(newrem + [num1/num2])
                        if ans:
                            break
                if ans:
                    break

            return ans

        return bt(cards)
        