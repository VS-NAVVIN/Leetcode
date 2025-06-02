class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        
        count = 0
        x = num
        while count < t:
            num += 1
            x += 2
            count += 1
        return x

        