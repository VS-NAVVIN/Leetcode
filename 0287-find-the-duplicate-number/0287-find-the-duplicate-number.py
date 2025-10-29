class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        n = Counter(nums)
        for i,j in n.items():
            if j > 1:
                return i