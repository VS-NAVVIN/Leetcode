class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        tot = 0
    
        while len(nums) > 0:
            if len(set(nums)) == len(nums):
                return tot
            else:
                nums = nums[3:]
                tot = tot + 1
        return tot




        