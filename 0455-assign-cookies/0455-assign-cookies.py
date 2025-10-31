class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        s.sort()
        g.sort()
        total = 0
        i = 0
        j = 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                total += 1
                i += 1
            j += 1

        return total