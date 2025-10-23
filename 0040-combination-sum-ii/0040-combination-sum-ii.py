class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        candidates.sort()

        def backtrack(start, path, total):

            if total > target:
                return
            if total == target:
                result.append(path[:])
                return
            prev = 0
            for i in range(start, len(candidates)):
                if prev == candidates[i]:
                    continue
                path.append(candidates[i])
                backtrack(i+1, path, total+candidates[i])
                prev = candidates[i]
                path.pop()

        backtrack(0,[],0)
        return result