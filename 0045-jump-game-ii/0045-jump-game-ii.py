class Solution:
    def jump(self, nums: List[int]) -> int:
        
        count = 0
        maxjump = 0
        lastjump = 0
        if len(nums) < 2:
            return 0
        for i in range(len(nums)):
            maxjump = max(maxjump, i + nums[i])
            if i == lastjump:
                count += 1
                lastjump = maxjump
                if lastjump >= len(nums)-1:
                    break
        return count
