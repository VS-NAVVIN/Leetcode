class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        if num < 2:
            return True
        low, high = 2, num // 2
        
        while low <= high:
            mid = (low + high) // 2
            guess_squared = mid * mid
            
            if guess_squared == num:
                return True
            elif guess_squared > num:
                high = mid - 1
            else:
                low = mid + 1
                
        return False




        