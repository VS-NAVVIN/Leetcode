from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq = Counter(s)
        total = 0
        vowels = {'a','e','i','o','u'}
        max_vowel = 0
        max_const = 0
        for char, count in freq.items():
            if char in vowels:
                max_vowel = max(max_vowel, count)
            else:
                max_const = max(max_const, count)
        return max_const+max_vowel