class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        count = {}

        # base case
        for ch in words[0]:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1
        
        # compare all other words
        for i in range(1, len(words)):
            word = words[i]
            localcount = {}
            # count word characters
            for ch in word:
                if ch in localcount:
                    localcount[ch] += 1
                else:
                    localcount[ch] = 1
            # compare local count with glocal count
            newcount = count.copy()
            for key in newcount:
                if key in localcount:
                    count[key] = min(count[key], localcount[key])
                else:
                    del count[key]
        
        # construct answer
        ans = []

        for key in count:
            ans.extend([key] * count[key])
        
        return ans