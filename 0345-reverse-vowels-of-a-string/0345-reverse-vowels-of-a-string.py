class Solution:
    def reverseVowels(self, s: str) -> str:
        chars = list(s)
        l, r = 0, len(s)-1
        vowels = set("aeiouAEIOU")

        while l < r:
            # find left vowel
            while l < len(s)-1 and chars[l] not in vowels:
                l += 1
                
            # find right vowel
            while r > 0 and chars[r] not in vowels:
                r -= 1
                
            # swap
            if l < r:
                chars[l], chars[r] = chars[r], chars[l]
                l += 1
                r -= 1

        return "".join(chars)
