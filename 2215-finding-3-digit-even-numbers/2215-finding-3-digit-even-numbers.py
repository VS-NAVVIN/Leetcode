from itertools import permutations
from typing import List
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        uniquenos = set()
        for num in permutations(digits,3):
            if num[0] == 0:
                continue
            if num[2] % 2 == 0:
                uniquenos.add(100*num[0] + 10*num[1] + num[2])
        return sorted(uniquenos)

        
        

        