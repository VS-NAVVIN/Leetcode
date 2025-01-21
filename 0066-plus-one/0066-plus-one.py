class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)
        result = digits[:]
        for i in range(l-1,-1,-1):
            if result[i] < 9:
                result[i] += 1
                return result
            result[i] = 0
        return [1] + result 






        