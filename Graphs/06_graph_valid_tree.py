class Solution:
    def valid_tree(self, n: int, edges: list[list[int]]) -> bool:
        if not n:
            return True
        
        adj = { i:[] for i in range(n) }

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False
            
            visit.add(i)
            for j in adj[i]:
                if j == prev: continue
                if not dfs(i = j, prev = i):
                    return False
            
            return True
        
        return dfs(i = 0, prev = -1) and n == len(visit)



if __name__ == "__main__":

    obj = Solution()

    n1 = 5 
    edges1 = [[0, 1], [0, 2], [0, 3], [1, 4]]
    print(obj.valid_tree(n = n1, edges = edges1))

    n2 = 5 
    edges2 = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    print(obj.valid_tree(n = n2, edges = edges2))

    

    