class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxi = mini = ans = nums[0]
        for i in nums[1:]:

            if i < 0:
                mini, maxi = maxi, mini
            maxi = max(maxi*i, i)
            mini = min(mini*i, i)
            ans = max(ans, maxi)

        return ans

            