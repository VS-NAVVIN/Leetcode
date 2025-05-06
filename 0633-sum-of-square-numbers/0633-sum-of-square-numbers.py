class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(c ** 0.5)
        while a <= b:
            target = a**2 + b**2
            if target == c:
                return True
            if target < c:
                a = a + 1
            else:
                b = b - 1       
        return False





        