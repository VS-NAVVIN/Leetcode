class Solution:
    def findMin(self, nums: List[int]) -> int:
        # low = 0
        # high = len(nums) - 1

        # while low <= high:

        #     mid =(low+high)//2
        
        nums.sort()
        return nums[0]