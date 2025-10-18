class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals.sort()
        merged = [intervals[0]]

        for current in intervals[1:]:
            last = merged[-1]
            if last[1] >= current[0]:
                last[1] = max(last[1], current[1])
            else:
                merged.append(current)
                
        return merged