class Solution:
    def isHappy(self, n: int) -> bool:
        def sumcalc(num):
            total = 0
            while num > 0:
                digit = num % 10
                total += digit ** 2
                num = num // 10
            return total
        
        visited = set()
        while n != 1 and n not in visited:
            visited.add(n)
            n = sumcalc(n)
        return n == 1


        
            


        