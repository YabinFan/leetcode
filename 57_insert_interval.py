class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        i, start, end = 0, 0, 1
        n = len(intervals)
        merged = []
        
        while i < n and intervals[i][end] < new_interval[start]:
            merged.append(intervals[i])
            i+=1
        
        while i< n and intervals[i][start] <= new_interval[end]:
            new_interval[start] = min(new_interval[start], intervals[i][start])
            new_interval[end] = max(new_interval[end], intervals[i][end])
            i+=1
        merged.append(new_interval)
        
        while i< n:
            merged.append(intervals[i])
            i+=1
        return merged
