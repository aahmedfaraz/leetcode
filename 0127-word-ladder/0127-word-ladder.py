from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        que = deque([(beginWord, 1)])
        visited = set([beginWord])

        def canSwitch(w1, w2):
            diff = 0
            for a, b in zip(w1, w2):
                if a != b:
                    diff += 1
                if diff > 1:
                    return False
            return diff == 1

        while que:
            word, steps = que.popleft()

            if word == endWord:
                return steps

            for nxt in wordSet:
                if nxt not in visited and canSwitch(word, nxt):
                    visited.add(nxt)
                    que.append((nxt, steps+1))
        
        return 0
