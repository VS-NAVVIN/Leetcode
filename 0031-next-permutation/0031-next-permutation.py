class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        j = len(nums)-1
        if i >= 0:
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        low = i+1
        high = len(nums)-1

        while low <= high:
            nums[low], nums[high] = nums[high], nums[low]
            low += 1
            high -= 1

        

        




            



        