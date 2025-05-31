class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        lens = len(s)-1
        lent = len(t)-1
        i = 0
        j = 0
    
        while i <= lens and j<= lent:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        
        return (len(s) == i)
                
            

        