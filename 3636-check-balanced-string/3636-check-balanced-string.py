class Solution:
    def isBalanced(self, num: str) -> bool:
        bal1 = 0
        bal2 = 0
        for i in range(0,len(num),2):
            bal1 += int(num[i])
        for j in range(1,len(num),2):
            bal2 += int(num[j])
        if bal1 == bal2:
            return True
        else:
            return False
        