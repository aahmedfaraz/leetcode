class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        lcounter = {}
        for ch in licensePlate:
            if ch.isalpha():
                ch = ch.lower()
                lcounter[ch] = lcounter[ch]+1 if ch in lcounter else 1 
        
        words.sort(key=len)
        
        for word in words:
            tcounter = lcounter.copy()
            for ch in word:
                ch = ch.lower()
                if ch in tcounter:
                    tcounter[ch] -= 1
                    if tcounter[ch] == 0:
                        del tcounter[ch]
            # print(word, tcounter)
            if len(tcounter) == 0:
                return word
        return ""
                        
            