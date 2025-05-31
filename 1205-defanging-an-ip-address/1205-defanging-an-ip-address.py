class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        temp = []

        for i in address:
            if i != ".":
                temp.append(i)
            else:
                temp.append("[.]")
        return "".join(temp)      