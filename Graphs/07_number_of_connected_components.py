class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n):
            res = n

            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]

            return res

        def union(n1, n2):
            p1, p2 = find(n = n1), find(n = n2)

            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            
            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1 = n1, n2 = n2)

        return res


if __name__ == "__main__":

    obj = Solution()

    n1 = 3
    edges1 = [[0,1], [0,2]]
    print(obj.countComponents(n = n1, edges = edges1))

    n2 = 6 
    edges2 = [[0,1], [1,2], [2, 3], [4, 5]]
    print(obj.countComponents(n = n2, edges = edges2))

    

    