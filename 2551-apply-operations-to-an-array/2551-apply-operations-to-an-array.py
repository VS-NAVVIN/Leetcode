class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        
        nzidx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[nzidx] = nums[i]
                nzidx += 1
        for i in range(nzidx,n):
            nums[i] = 0
            
        return nums
        