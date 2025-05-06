class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ans = []
        for i in range(0, l):
            ans.append(nums[nums[i]])
        return ans

        