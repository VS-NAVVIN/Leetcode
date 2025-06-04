class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        
        l = len(nums)
        tot = 0
        for i in range(l):
            for j in range(i+1,l):
                if nums[i] + nums[j] < target:
                    tot += 1
        return tot


        