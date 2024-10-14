class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
            
        temp = 0
        rev = 0
        original = x
        
        while x > 0:
            temp = x % 10
            x = x // 10
            rev = rev*10 + temp  
        return rev == original