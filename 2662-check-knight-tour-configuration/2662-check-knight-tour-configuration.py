class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        
        n = len(grid)
        
        pos = [0] * (n* n)
        
        for r in range(n):
            for c in range(n):
                move = grid[r][c]
                pos[move] = (r,c)
        
        if pos[0][0] != 0:
            return False
        
        for i in range(1, n*n):
            r1, c1 = pos[i-1]
            r2, c2 = pos[i]
            d1, d2 = abs(r1 - r2) , abs(c1 - c2)
            if not ((d1 == 1 and d2 == 2) or (d1 == 2 and d2 == 1)):
                return False
        
        return True

