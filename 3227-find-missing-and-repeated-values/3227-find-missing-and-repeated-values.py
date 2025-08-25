class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        freq = {}
        missing = 0
        repeated = 0
        n = len(grid)

        for row in grid:
            for num in row:
                if num in freq:
                    freq[num] += 1
                else:
                    freq[num] = 1

        for i in range(1, n*n+1):
            if i not in freq:
                missing = i
            elif i in freq and freq[i] > 1:
                repeated = i
        
        return [repeated, missing]



        