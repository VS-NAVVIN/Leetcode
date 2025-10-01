class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        word = " ".join(words[::-1])
        return word
        