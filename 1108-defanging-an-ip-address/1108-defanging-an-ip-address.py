class Solution:
    def defangIPaddr(self, address: str) -> str:
        arr = []
        for ch in address:
            if ch == '.':
                arr.append('[')
                arr.append('.')
                arr.append(']')
            else:
                arr.append(ch)

        return ''.join(arr)