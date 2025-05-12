class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def even(num):
            l = len(str(num))
            return l % 2 == 0
        count = 0
        for num in nums:
            if even(num):
                count += 1
        return count

            
            

        


        