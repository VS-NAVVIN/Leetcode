from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        w = Counter(words[0])

        for word in words[1:]:
            w &= Counter(word)

        return list(w.elements())
            

        


