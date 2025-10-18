class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        m = len(s1)
        n = len(s2)
        if m > n:
            return False
        
        cnt1 = Counter(s1)
        cnt2 = Counter(s2[:m])

        for i in range(n - m):

            if cnt1 == cnt2:
                return True
            
            cnt2[s2[i]] -= 1

            if cnt2[s2[i]] == 0:
                del cnt2[s2[i]]
            
            cnt2[s2[i+m]] += 1
        
        return cnt1 == cnt2
            