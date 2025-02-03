class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        if not intervals:
            return True

        intervals.sort(key = lambda i : i.start)
        prevEnd = intervals[0].end

        for interval in intervals[1:]:
            if interval.start >= prevEnd:
                prevEnd = interval.end
            else:
                return False
        return True




if __name__ == "__main__":

    obj = Solution()

    intervals1 = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
    print(obj.canAttendMeetings(intervals=intervals1))

    intervals2 = [Interval(5, 8), Interval(9, 15)]
    print(obj.canAttendMeetings(intervals=intervals2))