class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        paired_data = zip(names, heights)
        sorted_pairs = sorted(paired_data,key=lambda x: x[1], reverse=True)
        sorted_names = [name for name, _ in sorted_pairs]
        
        return sorted_names
        
        