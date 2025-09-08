class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        smallest_missing = 1

        for num in nums:
            if num == smallest_missing:
                smallest_missing += 1

        return smallest_missing      