class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I" : 1 , "V" : 5 , "X" : 10 , "L" : 50 , "C" : 100 , "D" : 500 , "M" : 1000}
        tot = 0
        prev = 0
        for i in reversed(s):
            cur = d[i]
            if cur < prev:
                tot -= cur
            else:
                tot += cur
            prev = cur
        return tot


            

        
        