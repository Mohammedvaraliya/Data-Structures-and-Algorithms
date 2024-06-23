# Data-Structures And Algorithms

### 01. Graph Data Structure

Graph Data Structure
Graphs in data structures are non-linear data structures made up of a finite number of nodes or vertices and the
edges that connect them.

```Bash
Example Graph:

            />  Paris
           /     |     \
          /      |      \
         /       |       \
        /        |        \> New York
Mumbai           |         />         \
        \        |        /            \
         \       |       /              \
          \      |      /                \
           \     |>    /                  \> Toronto
            \>  Dubai


The Routes:

    ("Mumbai", "Paris"),
    ("Mumbai", "Dubai"),
    ("Paris", "Dubai"),
    ("Paris", "New York"),
    ("Dubai", "New York"),
    ("New York", "Toronto")
```

**Explanation**

There is edges and the nodes in the graph data structure.
Mumbai, Dubai, Paris, New York and Toronto is the Nodes.
and edges are the lines which are pointing from one Node to the other.

Suppose i want to Know the path from "Mumbai" to "New York"

There is 3 possible paths available :

[['Mumbai', 'Paris', 'Dubai', 'New York'], ['Mumbai', 'Paris', 'New York'], ['Mumbai', 'Dubai', 'New York']]

And the shortest path is :

['Mumbai', 'Paris', 'New York']

### 02. Number of Islands

[Leetcode Problem URL](https://leetcode.com/problems/number-of-islands/description/)

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

```bash
Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

```bash
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

```
obj = Solution()

grid1 = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
print(obj.numIslands(grid=grid1))

grid2 = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print(obj.numIslands(grid=grid2))

grid3 = [
    ["1","1","1"],
    ["0","1","0"],
    ["1","1","1"]
]
print(obj.numIslands(grid=grid3))
```

**Explanation**

1. **Initialize Variables**:

   - Check if the grid is empty. If it is, return 0.
   - Initialize variables `rows` and `cols` to store the number of rows and columns of the grid, respectively.
   - Create a set `visit` to keep track of visited cells.
   - Initialize `islands` to 0 to count the number of islands.

2. **Breadth-First Search (BFS) Function**:

   - Define a BFS function `bfs` which takes `row` and `col` as arguments.
   - Use a deque `q` to implement the BFS queue.
   - Add the initial cell `(row, col)` to `visit` and `q`.
   - While the queue is not empty, pop a cell from the queue and check its four possible neighbors (up, down, left, right).
   - If a neighbor is within bounds, is land (`'1'`), and has not been visited, add it to the queue and mark it as visited.

3. **Main Loop**:

   - Loop through each cell in the grid.
   - If a cell is land and has not been visited, it is the start of a new island.
   - Call the BFS function to mark all cells connected to this cell.
   - Increment the `islands` counter.

4. **Return Result**:
   - After traversing the entire grid, return the number of islands.

#### Efficiency Analysis

- **Time Complexity**:

  - The grid has `m` rows and `n` columns.
  - Each cell is visited once, and each BFS operation considers up to 4 neighbors per cell.
  - The time complexity is $(O(m \times n))$ because we traverse every cell in the grid once.

- **Space Complexity**:
  - The space complexity is also $(O(m \times n))$ due to the `visit` set and the queue used in BFS, which in the worst case can store all cells in the grid.
  - Additionally, the recursive stack of BFS can go up to the size of the grid in the worst case.

### 03. Clone Graph

[Leetcode Problem URL](https://leetcode.com/problems/clone-graph/)

Given a node in a connected undirected graph, return a deep copy of the graph.

Each node in the graph contains an integer value and a list of its neighbors.

```bash
class Node {
    public int val;
    public List<Node> neighbors;
}
```

The graph is shown in the test cases as an adjacency list. An adjacency list is a mapping of nodes to lists, used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

For simplicity, nodes values are numbered from 1 to n, where n is the total number of nodes in the graph. The index of each node within the adjacency list is the same as the node's value (1-indexed).

The input node will always be the first node in the graph and have 1 as the value.

```bash
Example 1:

    1 ----------- 2
    |             |
    |             |
    |             |
    |             |
    4 ----------- 3

Input: adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
Output: [[2, 4], [1, 3], [2, 4], [1, 3]]

Explanation: There are 3 nodes in the graph.
Node 1: val = 1 and neighbors = [2, 4].
Node 2: val = 2 and neighbors = [1, 3].
Node 3: val = 3 and neighbors = [2, 4].
Node 4: val = 4 and neighbors = [1, 3].
```

![Image 2](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/96c7fb34-26e8-42e0-5f5d-61b8b8c96800/public)

```bash
Example 2:

Input: adjList = [[]]
Output: [[]]

Explanation: The graph has one node with no neighbors.
```

```bash
Example 3:

Input: adjList = []
Output: []

Explanation: The graph is empty.
```

**Explanation**

First, we define the `Node` class to represent a node in the graph.

```python
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
```

#### Solution Class

The `Solution` class contains the `cloneGraph` method to clone the graph.

1. **Initialization**:

   - `oldToNew` is a dictionary(HashMap) that maps original nodes to their copies.

2. **DFS Function**:

   - This is a helper function that performs a Depth-First Search (DFS) to traverse and copy the graph.
   - If the node has already been copied (exists in `oldToNew`), it returns the copied node to avoid cycles.
   - Otherwise, it creates a new node (`copy`), adds it to the `oldToNew` dictionary, and then recursively copies all the neighbors.

3. **Clone Graph**:

   - Starts the cloning process by calling the `dfs` function with the input node if the node is not `None`.

#### Creating the Graph from Adjacency List

The `createGraph` function converts an adjacency list into a graph represented by `Node` objects.

1. **Check for Empty List**:

   - If the adjacency list is empty, return `None`.

2. **Create Nodes**:

   - Create a list of Node objects where each node's value corresponds to its index (1-indexed). Nodes' values are numbered from 1 to n, where n is the total number of nodes in the graph. The index of each node within the adjacency list matches the node's value (1-indexed).
   - For example, if the graph has a total of 5 nodes (n=5), the values of the nodes should be 1, 2, 3, 4, and 5. Each node will have its respective neighbors (adjacent nodes) as defined in the adjacency list.

3. **Assign Neighbors**:

   - For each node, populate its `neighbors` list using the adjacency list.

4. **Return Start Node**:
   - Return the first node in the list as the starting node of the graph.

#### Efficiency Analysis

- **Time Complexity**:

  - The time complexity is $O(V + E)$, where V is the number of vertices (nodes) and E is the number of edges.
  - Each node and each edge is visited once during the DFS traversal.

- **Space Complexity**:

  - The space complexity is $O(V)$ due to the space needed to store the copy of each node and the recursion stack.

### 04. Pacific Atlantic Water Flow

[Leetcode Problem URL](https://leetcode.com/problems/pacific-atlantic-water-flow/description/)

There is an `m x n` rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an `m x n` integer matrix `heights` where `heights[r][c]` represents the height above sea level of the cell at coordinate `(r, c)`.

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates `result` where `result[i] = [ri, ci]` denotes that rain water can flow from cell `(ri, ci)` to both the Pacific and Atlantic oceans.

![Image 1](https://assets.leetcode.com/uploads/2021/06/08/waterflow-grid.jpg)

```bash
Example 1:

Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
```

```bash
Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
```

**Explanation**

### 04. Pacific Atlantic Water Flow

[Leetcode Problem URL](https://leetcode.com/problems/pacific-atlantic-water-flow/description/)

I've employed Depth-First Search (DFS) to determine which cells can flow to both oceans.

1. **Initialization**:

   - Determine the number of rows and columns in the grid.
   - Create two sets, `pac` and `atl`, to keep track of cells that can reach the Pacific and Atlantic Oceans, respectively.

2. **Depth-First Search (DFS) Function**:

   - The `dfs` function is used to explore all possible cells that water can flow to from a given starting cell. It takes the current cell's row and column, a set to track visited cells, and the previous cell's height as parameters.
   - The base case checks whether the cell is out of bounds, has already been visited, or its height is less than the previous cell's height.
   - If the cell passes these checks, it's added to the visited set, and the DFS continues to the neighboring cells (up, down, left, right).

3. **Perform DFS for All Boundary Cells**:

   - Perform DFS starting from each cell in the first row and the last row for the Pacific and Atlantic Oceans, respectively.
   - Perform DFS starting from each cell in the first column and the last column for the Pacific and Atlantic Oceans, respectively.

4. **Find Intersection of Both Sets**:

   - The final result is the intersection of the cells that can reach both the Pacific and Atlantic Oceans.
   - `.intersection()` method: This method is used on sets to find the elements that are common to both sets. In other words, it returns a new set containing elements that exist in both `pac` and `atl`.

#### Efficiency Analysis

- **Time Complexity**:
  - The algorithm runs a DFS from each cell that touches the oceans, visiting each cell in the grid at most once. Therefore, the time complexity is $O(m \times n)$, where $(m)$ is the number of rows and $(n)$ is the number of columns.
- **Space Complexity**:
  - The space complexity is $(O(m \times n))$ for the visited sets and the recursion stack in the worst case
