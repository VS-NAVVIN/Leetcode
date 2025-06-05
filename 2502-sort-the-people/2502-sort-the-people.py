class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res = []

        while heights:
            maxi = max(heights)
            idx = heights.index(maxi)
            res.append(names[idx])
            heights.pop(idx)
            names.pop(idx)
        return res
        