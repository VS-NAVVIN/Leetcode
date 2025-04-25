class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        v1 = 1
        v2 = 2
        current = 0

        for i in range(3,n+1):
            current = v1 + v2
            v1, v2 = v2, current
        return current
            


        