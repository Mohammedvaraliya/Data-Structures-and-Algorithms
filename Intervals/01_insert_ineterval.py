class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval)

        return res




if __name__ == "__main__":

    obj = Solution()

    intervals1 = [[1,3],[4,6]]
    newInterval1 = [2,5]
    print(obj.insert(intervals=intervals1, newInterval=newInterval1))

    intervals2 = [[1,2],[3,5],[9,10]]
    newInterval2 = [6,7]
    print(obj.insert(intervals=intervals2, newInterval=newInterval2))