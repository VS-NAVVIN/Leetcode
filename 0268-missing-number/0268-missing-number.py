from collections import Counter
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        n = len(nums)
        for i in range(0,n):
            if i != nums[i]:
                return i
        return n