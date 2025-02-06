class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        print(start)
        print(end)

        result, count = 0, 0
        s, e = 0, 0

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            result = max(result, count)

        return result




if __name__ == "__main__":

    obj = Solution()

    intervals1 = [Interval(0,40), Interval(5,10), Interval(15,20)]
    print(obj.minMeetingRooms(intervals=intervals1))

    intervals2 = [Interval(4,9)]
    print(obj.minMeetingRooms(intervals=intervals2))