class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        n = len(nums)
        nums = list(nums)
        nums.sort(reverse = True)
        if n >= 3:
            return nums[2]
        else:
            return nums[0]
        