import math

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        def add_spaces(string, maxWidth, lastLine):
            words = string.split(' ')
            total_words = len(words)
            fill_spaces = total_words - 1
            total_letters = len(string) - fill_spaces
            available_spaces = maxWidth - total_letters

            print('String = "' + string + '", maxWidth = ', maxWidth)
            print('Fill spaces = ', fill_spaces, ', total letters = ', total_letters)
            print('available spaces = ', available_spaces)

            res = ""
            if lastLine or total_words == 1: # should be left justified
                print('str is last line')
                res = string + (" " * (maxWidth - len(string)))
                print('--RES = "' + res + '"')
            else: # string with 1+ words
                print('str is initial lines')
                # fill gap between words
                for i in range(len(words) - 1):
                    gap_used = math.ceil(available_spaces / fill_spaces)
                    res += (words[i] + (" " * gap_used))
                    available_spaces -= gap_used
                    fill_spaces -= 1
                    print('For "' + words[i] + '" gap length used = ', gap_used, ', available spaces = ', available_spaces)
                # add remaining spaces between last word
                remaining_spaces = " " * available_spaces
                print('remaining spaces length = ', len(remaining_spaces))
                res += remaining_spaces + words[-1]
                print('--RES = "' + res + '"')
            
            print('RES = "' + res + '"')
            print('------')
            return res
        
        # For only 1 word
        total_words = len(words)
        if total_words == 1: return [ words[0] + (" " * (maxWidth - len(words[0]))) ]
        
        lines = []
        curr_str = words[0]
        for i in range(1, total_words):
            if (len(curr_str) + len(words[i]) + 1) > maxWidth:
                lines.append(add_spaces(curr_str, maxWidth, False))
                curr_str = words[i]
            else:
                curr_str += f' {words[i]}'
        
        # fencepost case
        if curr_str != "":
            lines.append(add_spaces(curr_str, maxWidth, True))
            
        return lines