class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=[]
        s=s.rstrip()
        for i in range(len(s)-1,-1,-1):
            # print(i)
            if s[i] ==' ':
                break
            l.append(s[i])
            
        return len(l)        
        