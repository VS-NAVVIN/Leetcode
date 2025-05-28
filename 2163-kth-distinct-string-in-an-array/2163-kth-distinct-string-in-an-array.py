from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = Counter(arr)

        distinct = []
        for i,j in freq.items():
            if j == 1:
                distinct.append(i)
        
        if k <= len(distinct):
            return distinct[k-1]
        return ""
        






        