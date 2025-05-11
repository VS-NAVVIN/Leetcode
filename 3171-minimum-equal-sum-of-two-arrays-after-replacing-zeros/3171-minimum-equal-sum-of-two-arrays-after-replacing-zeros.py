class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        n1 = nums1.count(0)
        n2 = nums2.count(0)
        
        tot = max(sum1+n1, sum2+n2)
        if sum1 != tot and n1 == 0 or sum2 != tot and n2 == 0:
            return -1
        return tot
                 

        