class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        output = [0]*n

        prefix = 1

        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        sufix = 1

        for i in reversed(range(n)):
            output[i] *= sufix
            sufix *= nums[i]
        

        return output



