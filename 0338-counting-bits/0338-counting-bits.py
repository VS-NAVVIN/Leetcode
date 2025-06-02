class Solution:
    def countBits(self, n: int) -> List[int]:
        lst = []
        for i in range(n+1):
            binary=bin(i)[2:]
            count=0
            for char in binary:
                if char=="1":
                    count+=1
            lst.append(count)
        return lst
            
        