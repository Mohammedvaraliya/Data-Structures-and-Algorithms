class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        pass



if __name__ == "__main__":

    obj = Solution()

    n1 = 3
    edges1 = [[0,1], [0,2]]
    print(obj.countComponents(n = n1, edges = edges1))

    n2 = 6 
    edges2 = [[0,1], [1,2], [2, 3], [4, 5]]
    print(obj.countComponents(n = n2, edges = edges2))

    

    