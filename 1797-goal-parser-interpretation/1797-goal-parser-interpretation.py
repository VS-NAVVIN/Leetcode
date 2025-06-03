class Solution:
    def interpret(self, command: str) -> str:
        lst = []
        i = 0
        while i < len(command):
            if i == 'G':
                lst.append('G')
            elif command[i:i+2] == '()':
                lst.append('o')
                i += 1
            elif command[i:i+4] =='(al)':
                lst.append('al')
                i += 3
            else:
                lst.append(command[i])
            i += 1
        return "".join(lst)

