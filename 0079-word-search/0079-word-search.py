class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        seen = set()
        k = 0

        def dfs(i,j,k):
            if k == len(word):
                return True
            if (i < 0 or i >= rows or j < 0 or j >= cols or 
                board[i][j] != word[k] or (i,j) in seen):
                return False
            
            seen.add((i, j))

            found = (
            dfs(i+1, j, k+1) or
            dfs(i-1, j, k+1) or
            dfs(i, j+1, k+1) or
            dfs(i, j-1, k+1))

            seen.remove((i,j))

            return found

        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,k):
                    return True
        
        return False





            
        