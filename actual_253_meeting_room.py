import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # [[0, 30],[5, 10],[15, 20]]
        # [0, 30]
        # [5, 10],[15, 20]
        if not intervals:
            return 0
        intervals.sort()
        meetings = []
        heapq.heappush(meetings, intervals[0][1])
        for i in range(1, len(intervals)):
            if meetings[0] > intervals[i][0]:
                heapq.heappush(meetings, intervals[i][1])
            else:
                heapq.heappop(meetings)
                heapq.heappush(meetings, intervals[i][1])
        return len(meetings)
            
