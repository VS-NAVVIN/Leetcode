import math
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        gap = math.ceil((m+n)/2)
        while gap > 0:
            i = 0
            j = gap
            while j < (m+n):
                if i < m:
                    a = nums1[i]
                else:
                    a = nums2[i-m]
                if j < m:
                    b = nums1[j]
                else:
                    b = nums2[j-m]
                if a > b:
                    if i < m and j < m:
                        nums1[i], nums1[j] = nums1[j], nums1[i]
                    elif i < m and j >= m:
                        nums1[i] , nums2[j-m] = nums2[j-m], nums1[i]
                    else:
                        nums2[i-m], nums2[j-m] = nums2[j-m], nums2[i-m]

                i += 1
                j += 1
            
            if gap == 1:
                gap = 0
            else:
                gap = math.ceil(gap/2)
        
        nums1[m:] = nums2

                




        