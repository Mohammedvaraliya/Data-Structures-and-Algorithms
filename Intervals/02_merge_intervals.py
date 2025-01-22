class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        
        return output




if __name__ == "__main__":

    obj = Solution()

    intervals1 = [[1,3],[2,6],[8,10],[15,18]]
    print(obj.merge(intervals=intervals1))

    intervals2 = [[1,4],[4,5]]
    newInterval2 = [6,7]
    print(obj.merge(intervals=intervals2))