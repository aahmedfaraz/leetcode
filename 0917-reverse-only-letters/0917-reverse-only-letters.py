class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        arr = list(s)
        i, j = 0, len(s)-1

        while i < j:
            while i < j and not arr[i].isalpha():
                i += 1
            while j > i and not arr[j].isalpha():
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        
        return ''.join(arr)