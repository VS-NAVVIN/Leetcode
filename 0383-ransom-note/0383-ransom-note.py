class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        m = Counter(magazine)
        r = Counter(ransomNote)

        for i, j in r.items():
            if m[i] < j:
                return False
        return True
