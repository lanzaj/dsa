class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newStart = newInterval[0]
        newEnd = newInterval[1]

        if len(intervals) == 0:
            return [newInterval]

        ret = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newStart:
            curStart, curEnd = intervals[i]
            ret.append([curStart, curEnd])
            i += 1
        
        if i == len(intervals):
            ret.append(newInterval)
            return ret
        
        curStart, curEnd = intervals[i]
        start = min(curStart, newStart)
        end = newEnd
        while i < len(intervals) and intervals[i][0] <= newEnd:
            curStart, curEnd = intervals[i]
            end = max(curEnd, newEnd)
            i += 1
        ret.append([start, end])

        while i < len(intervals):
            curStart, curEnd = intervals[i]
            ret.append([curStart, curEnd])
            i += 1

        return ret
