class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = set()
        
        def dfs(curr, rem):
            nonlocal res
            
            if not rem:
                if curr.count('.') == 3:
                    res.add(curr)
                return
            
            if curr.count('.') >= 3:
                return
            
            for i in range(1, 4):
                if i > len(rem):
                    break
                
                num = rem[:i]
                
                # fix leading zero condition
                if (len(num) > 1 and num[0] == '0'):
                    continue
                
                if int(num) <= 255:
                    dfs(curr + ('.' if curr else '') + num, rem[i:])
        
        dfs("", s)
        return list(res)