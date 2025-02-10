class Solution:
    def clearDigits(self, s: str) -> str:
        string = []
        for i in s:
            if not i.isdigit():
                string.append(i)
            else:
                string.pop()
        return "".join(string)
        