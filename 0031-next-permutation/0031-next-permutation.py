class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        i = j = n-1

        while i > 0 and nums[i-1] >= nums[i]:
            i = i - 1
         
        if i == 0:
            nums.reverse()
            return

        while nums[j] <= nums[i-1]:
            j = j - 1
        
        nums[i-1], nums[j] = nums[j], nums[i-1]

        nums[i:] = reversed(nums[i:])



        

        




            



        