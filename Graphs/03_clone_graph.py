class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy
        
        return dfs(node = node) if node else None

def createGraph(adjList):
    if not adjList:
        return None

    nodes = [Node(i) for i in range(1, len(adjList) + 1)]

    for i, neighbors in enumerate(adjList):
        nodes[i].neighbors = [nodes[n - 1] for n in neighbors]

    return nodes[0] if nodes else None

def printGraph(node):
    visited = set()
    def dfs(node):
        if node.val in visited:
            return
        visited.add(node.val)
        print(f'Node {node.val}: {[n.val for n in node.neighbors]}')
        for neighbor in node.neighbors:
            dfs(neighbor)
            
    dfs(node)


if __name__ == "__main__":
    obj = Solution()
    
    adjList1 = [[2, 4], [1, 3], [2, 4], [1, 3]]
    graph1 = createGraph(adjList1)
    cloned_graph1 = obj.cloneGraph(graph1)
    print("Original Graph:")
    printGraph(graph1)
    print("\nCloned Graph:")
    printGraph(cloned_graph1)
    
    adjList2 = [[2],[1,3],[2]]
    graph2 = createGraph(adjList2)
    cloned_graph2 = obj.cloneGraph(graph2)
    print("Original Graph:")
    printGraph(graph2)
    print("\nCloned Graph:")
    printGraph(cloned_graph2)
    
    
    
    
