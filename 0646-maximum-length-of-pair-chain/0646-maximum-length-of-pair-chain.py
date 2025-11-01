class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        start = float("-inf")
        total = 0
        for pair in pairs:
            if pair[0] > start:
                total += 1
                start = pair[1]

        return total
                