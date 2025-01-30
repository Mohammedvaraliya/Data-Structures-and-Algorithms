class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:

        intervals.sort(key = lambda i : i[0])
        result = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                result += 1
                prevEnd = min(end, prevEnd)
        
        return result




if __name__ == "__main__":

    obj = Solution()

    intervals1 = [[1,3],[2,6],[8,10],[15,18]]
    print(obj.eraseOverlapIntervals(intervals=intervals1))

    intervals2 = [[1,2],[1,2],[1,2]]
    print(obj.eraseOverlapIntervals(intervals=intervals2))

    intervals3 = [[1,2],[2,3]]
    print(obj.eraseOverlapIntervals(intervals=intervals3))