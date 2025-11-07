class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        maxtot = [1]*(len(nums))

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    maxtot[i] = max(maxtot[i], maxtot[j]+1)
                    
        return max(maxtot)