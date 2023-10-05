"""
DIFFICULTY : hard
TAGS : array, string, simulation
"""
class Solution:
    def fullJustify(self, words: List[str], mw: int) -> List[str]:
        lines = [] 
        ptr = 0 
        cur_words_len = 0 
        temp = []
        
        while ptr < len(words):
            word = words[ptr]
            
            if (cur_words_len + len(word)) <= mw:
                temp.append(word)
                cur_words_len += len(word) + 1
                ptr += 1
            else: 
                line = ""
                diff = mw - cur_words_len + len(temp) 

                if len(temp) == 1: 
                    line += temp[0] + " " * diff 
                else: 
                    for j in range(len(temp)):
                        line_word = temp[j]
                        remaining_words = len(temp) - (j + 1)
                        req_spaces = 0
                        if(remaining_words) :
                            req_spaces = math.ceil(diff / remaining_words)
                        line += line_word + " " * req_spaces
                        diff -= req_spaces 
                lines.append(line) 
                temp = []
                cur_words_len = 0


        if temp: 
            diff = mw - cur_words_len + 1
            line = " ".join(temp) + " " * diff
            lines.append(line)
        return lines
                    
                    










