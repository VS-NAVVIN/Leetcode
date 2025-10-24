class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        result = []

        def palindrome(substr):
            return substr == substr[::-1]

        def backtrack(start, path):

            if start == len(s):
                result.append(path[:])
                return 
            
            for end in range(start+1, len(s) + 1):
                substr = s[start:end]
                if palindrome(substr):
                    path.append(substr)
                    backtrack(end, path)
                    path.pop()
        
        backtrack(0,[])
        return result

