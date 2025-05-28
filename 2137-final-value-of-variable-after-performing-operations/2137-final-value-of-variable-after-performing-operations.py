class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        dicty = {"X++" : 1 , "++X" : 1 , "X--" : -1 , "--X" : -1}
        total = 0
        for i in operations:
            total += dicty[i]
        return total



        