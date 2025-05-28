class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        arr = []
        for i in s.split():
            if i.isdigit():
                arr.append(int (i))
        
        for i in range(len(arr)-1):
            if arr[i] >= arr[i+1]:
                return False
        return True