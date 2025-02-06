class Solution:
    def isValid(self, s: str) -> bool:
        map = { ')' : '(' , '}' : '{' , ']' : '['}
        stack = []
        
        for i in s:
            if i in map.values():
                stack.append(i)
            elif i in map.keys():
                if len(stack) == 0 or map[i] != stack.pop():
                    return False
            else:
                return False
        return len(stack) == 0

        




        