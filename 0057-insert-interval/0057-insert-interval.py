class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals.sort()
        if len(intervals) == 0:
            return [newInterval]
        merged = [intervals[0]]

        l = intervals[0]
        if len(intervals) == 1:
            if l[0] >= newInterval[0]:
                l[0] = max(l[0], newInterval[0]) 
            if l[1] >= newInterval[0]:
                l[1] = max(l[1], newInterval[1])
            else:
                merged.append(newInterval)
            return merged

        for current in intervals[1:]:   
            last = merged[-1]
            if last[1] >= newInterval[0]:
                last[1] = max(newInterval[1], last[1])
            if last[1] >= current[0]:
                last[1] = max(last[1], current[1])
            else:
                merged.append(current)
        return merged