class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        
        l = []
        total = 1
        if num <= 1:
            return False

        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                total += i
                if i != num//i:
                    total += num//i
        return num == total



        