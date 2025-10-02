class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        c = Counter(nums)
        if target in c.keys():
            return True
        else:
            return False                
