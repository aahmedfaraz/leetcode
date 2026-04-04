class Solution: 
    def decodeCiphertext(self, encodedText: str, rows: int) -> str: 
        cols = len(encodedText) // rows 
        originalText = "" 
        spaces = 0 
        
        for col in range(cols):
            while col < len(encodedText): 
                if encodedText[col] == " ": 
                    spaces += 1 
                else: 
                    originalText += f'{' '*spaces}{encodedText[col]}' 
                    spaces = 0 
                col += (cols + 1) 
        return originalText
        
# Time = O(n)
# Space = O(n)