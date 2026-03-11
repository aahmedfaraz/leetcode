class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words: return []

        wordSize = len(words[0])
        winSize = wordSize * len(words)
        freqMap = {}
        for word in words:
            if word in freqMap:
                freqMap[word] += 1
            else:
                freqMap[word] = 1
        res = []

        # Iterate full string, from all letters of a word
        for i in range(wordSize):
            start = i
            # Before Iterating a window, make sure we have a window left
            while start + winSize <= len(s):
                # Iterate a window
                currMap = freqMap.copy()
                found = True
                for j in range(start, start + winSize, wordSize):
                    newWord = s[j:j+wordSize]
                    if newWord in currMap and currMap[newWord] > 0:
                        currMap[newWord] -= 1 # this word is no more allowed in the same window
                    else:
                        found = False
                        break
                if found:
                    res.append(start)
                start += wordSize

        return res