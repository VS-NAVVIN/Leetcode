class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = float('-inf')
        currentsum = 0
        for i in nums:
            currentsum += i
            maxsum = max(currentsum,maxsum)
            if currentsum < 0:
                currentsum = 0
        return maxsum


        