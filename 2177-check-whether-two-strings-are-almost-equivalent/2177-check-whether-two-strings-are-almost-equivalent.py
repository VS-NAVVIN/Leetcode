class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        w1 = Counter(word1)
        w2 = Counter(word2)
        all_char=set(w1.keys()).union(set(w2.keys()))
        for i in all_char:
            if abs(w1[i]-w2[i])>3:
                return False
        return True
        