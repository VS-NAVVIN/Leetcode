class Solution:
    def reverseDegree(self, s: str) -> int:
        
        tot = 0

        for i, char in enumerate(s):
            
            res_pos = 26 - (ord(char) - ord('a'))
            tot += res_pos*(i+1)
        return tot
