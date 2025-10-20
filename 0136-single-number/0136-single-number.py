class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = Counter(nums)
        for i, count in n.items():
            if count == 1:
                return i
        return 0