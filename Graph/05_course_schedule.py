class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        # Map each course to prereq list, For example, if numCourses = 3, prereq list as 0: [], 1: [], 2: [].
        preMap = { i:[] for i in range(numCourses) }

        for course, prerequisite in prerequisites:
            preMap[course].append(prerequisite)

        visitSet = set()

        def dfs(course):
            if course in visitSet:
                return False
            
            if preMap[course] == []:
                return True
            
            visitSet.add(course)
            for prerequisite in preMap[course]:
                if not dfs(course = prerequisite): return False
            
            visitSet.remove(course)
            preMap[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course = course): return False
        return True
        







if __name__ == "__main__":

    obj = Solution()
    
    numCourses1 = 2
    prerequisites1 = [[1,0]]
    print(obj.canFinish(numCourses = numCourses1, prerequisites = prerequisites1))
    
    numCourses2 = 2
    prerequisites2 = [[1,0],[0,1]]
    print(obj.canFinish(numCourses = numCourses2, prerequisites = prerequisites2))
    