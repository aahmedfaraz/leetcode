import math

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        total_words = len(words)
        if total_words == 1: return [ words[0] + (" " * (maxWidth - len(words[0]))) ]

        def add_spaces(string, maxWidth, lastLine):
            words = string.split(' ')
            total_words = len(words)
            fill_spaces = total_words - 1
            total_letters = len(string) - fill_spaces
            available_spaces = maxWidth - total_letters

            if lastLine or total_words == 1: # should be left justified
                return string + (" " * (maxWidth - len(string)))

            res = []

            # fill gap between words
            for i in range(len(words) - 1):
                gap_used = math.ceil(available_spaces / fill_spaces)
                res.append((words[i] + (" " * gap_used)))
                available_spaces -= gap_used
                fill_spaces -= 1

            # add remaining spaces before last word
            remaining_spaces = " " * available_spaces
            res.append(remaining_spaces + words[-1])
            return "".join(res)
        
        lines = []

        # create lines below the limit of maxWidth
        curr_str = [words[0]]
        for i in range(1, total_words):
            if (len("".join(curr_str)) + len(words[i]) + 1) > maxWidth:
                lines.append(add_spaces("".join(curr_str), maxWidth, False))
                curr_str = [words[i]]
            else:
                curr_str.append(f' {words[i]}')
        
        # last line
        lines.append(add_spaces("".join(curr_str), maxWidth, True))
            
        return lines

# time complexity = O(L), where L = total characters in all words
# space complexity = O(L)