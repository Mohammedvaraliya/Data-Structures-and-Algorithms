# Graphs Data-Structures and Algorithms

## 01. Graph Data Structure

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

### Explanation

There is edges and the nodes in the graph data structure.
Mumbai, Dubai, Paris, New York and Toronto is the Nodes.
and edges are the lines which are pointing from one Node to the other.

Suppose i want to Know the path from "Mumbai" to "New York"

There is 3 possible paths available :

[['Mumbai', 'Paris', 'Dubai', 'New York'], ['Mumbai', 'Paris', 'New York'], ['Mumbai', 'Dubai', 'New York']]

And the shortest path is :

['Mumbai', 'Paris', 'New York']

---

---

## 02. Number of Islands

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

### Explanation

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

---

---

## 03. Clone Graph

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

### Explanation

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

---

---

## 04. Pacific Atlantic Water Flow

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

### Explanation

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
  - The space complexity is $(O(m \times n))$ for the visited sets and the recursion stack in the worst case.

---

---

## 05. Course Schedule

[Leetcode Problem URL](https://leetcode.com/problems/course-schedule/description/)

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course $b_i$ first if you want to take course $a_i$.

For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.
Return `true` if you can finish all courses. Otherwise, return `false`.

```bash
Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
```

```bash
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
```

### Explanation

The problem can be visualized as detecting cycles in a directed graph where each course is a node and each prerequisite is a directed edge. If there is a cycle, it is impossible to complete all courses.

I've employed Depth-First Search (DFS) to detect cycles in the graph.

1. **Graph Representation**:

   - Initialize `preMap` to map each course to its list of prerequisites.
   - Example: For `numCourses = 3`, initialize as `{0: [], 1: [], 2: []}`.
   - Populate `preMap` with the prerequisites:

2. **DFS Function**:

   - Define the `dfs` function which will perform the depth-first search to detect cycles.
   - If a course is already in `visitSet`, it means there's a cycle:
     ```python
     if course in visitSet:
         return False
     ```
   - If a course has no prerequisites, it can be completed:
     ```python
     if preMap[course] == []:
         return True
     ```
   - Add the course to `visitSet` and recursively check all its prerequisites:
     ```python
     visitSet.add(course)
     for prerequisite in preMap[course]:
         if not dfs(prerequisite):
             return False
     visitSet.remove(course)
     preMap[course] = []  # Clear prerequisites to mark it as completed
     return True
     ```

3. **DFS Execution**:
   - Iterate over each course and run `dfs`. If any call returns `False`, there's a cycle:
     ```python
     for course in range(numCourses):
         if not dfs(course):
             return False
     return True
     ```

#### Efficiency Analysis

- **Time Complexity**:

  - Building the `preMap` takes $O(p)$, where $p$ is the number of prerequisites.
  - Each course is visited once, and during the visit, all its prerequisites are checked. Thus, the DFS traversal takes $O(n + p)$ time, where $n$ is the number of courses.
  - Overall, the time complexity is $O(n + p)$.

- **Space Complexity**:
  - The `preMap` dictionary uses $O(n + p)$ space.
  - The `visitSet` set uses $O(n)$ space.
  - The recursion stack for DFS can go up to $O(n)$ depth.
  - Overall, the space complexity is $O(n + p)$.

---

---

## 06. Graph Valid Tree

[Leetcode Problem URL](https://leetcode.com/problems/graph-valid-tree/description/)
[Lintcode Problem URL](https://www.lintcode.com/problem/178/)

Given `n` nodes labeled from `0` to `n - 1` and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

```bash
Example 1:

Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true
```

```bash
Example 2:

Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: false
```

### Explanation

The problem can be solved using Depth-First Search (DFS) to check for two conditions:

1. The graph is connected (all nodes are reachable from any node).
2. The graph is acyclic (no cycles).

The following solution uses DFS to check these conditions.

1. **Adjacency List**:

   - Initialize `adj` to map each node to its list of connected nodes.
   - Example: For `n = 5`, initialize as `{0: [], 1: [], 2: [], 3: [], 4: []}`.
   - Populate `adj` with the edges:
     ```python
     for n1, n2 in edges:
         adj[n1].append(n2)
         adj[n2].append(n1)
     ```

2. **DFS Function**:

   - Define the `dfs` function which will perform the depth-first search to check connectivity and detect cycles.
   - If a node is already visited, it means there's a cycle:
     ```python
     if i in visit:
         return False
     ```
   - Add the node to `visit` and recursively check all its connected nodes:
     ```python
     visit.add(i)
     for j in adj[i]:
         if j == prev:  # Skip the node we came from
             continue
         if not dfs(j, i):
             return False
     ```
   - If no cycles are detected, return `True`.

3. **DFS Execution**:
   - Start DFS from node `0` and ensure all nodes are visited:
     ```python
     return dfs(0, -1) and n == len(visit)
     ```
   - If any node is not visited, the graph is not connected and thus not a valid tree.

#### Efficiency Analysis

- **Time Complexity**: The solution iterates over all nodes and edges once, giving a time complexity of $O(V + E)$.
- **Space Complexity**: The adjacency list and the recursion stack both contribute to the space complexity, which is $O(V + E)$.

---

---

## 07. Number of Connected Components in an Undirected Graph

[Leetcode Problem URL](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/)
[Lintcode Problem URL](https://www.lintcode.com/problem/3651/)
[A Blog to Understand Union Find Algorithm](https://www.hackerearth.com/practice/notes/disjoint-set-union-union-find/)

There is an undirected graph with `n` nodes. There is also an `edges` array, where `edges[i] = [a, b]` means that there is an edge between node `a` and node `b` in the graph.

Return the total number of connected components in that graph.

```bash
Example 1

Input:
n=3
edges=[[0,1], [0,2]]

Output:
1
```

```bash
Example 2

Input:
n=6
edges=[[0,1], [1,2], [2, 3], [4, 5]]

Output:
2
```

To solve this problem, I've used Union-Find (or Disjoint Set Union, DSU) data structure. The Union-Find data structure helps us efficiently manage and merge sets of elements, which is useful for determining connected components.

1. **Initialize Parent and Rank Arrays**:

   - `par = [0, 1, 2, ..., n-1]`: Each node is initially its own parent.
   - `rank = [1, 1, 1, ..., 1]`: Each node starts with a rank of `1`.

2. **Find Function**:

   - The `find` function traverses up the parent chain to find the root of a node. Path compression is applied by setting the parent of each visited node directly to the root.

3. **Union Function**:

   - The `union` function merges two sets. It uses the rank to attach the smaller tree under the larger tree to keep the structure flat. If two nodes are already in the same set, no action is taken, and it returns `0`. If they are in different sets, it merges them and returns `1`.

4. **Count Components**:

   - Start with `res = n` (each node is its own component).
   - For each edge `[n1, n2]`, call `union(n1, n2)`. If a merge occurs (return value `1`), decrease `res` by `1`.

#### Example Walkthrough

Consider a graph with `n = 6` nodes and edges `[[0, 1], [1, 2], [2, 3], [4, 5]]`.

1. **Initialization**:

   - Each node is its own parent.
   - The rank of each node is initially 1.

   ```python
   par = [0, 1, 2, 3, 4, 5]
   rank = [1, 1, 1, 1, 1, 1]
   ```

2. **Union(0, 1)**:

   - `find(0)` returns `0` (0 is its own parent).
   - `find(1)` returns `1` (1 is its own parent).
   - Since they are in different subsets, union them:
     - Make `0` the parent of `1`.
     - Update the rank of `0` by adding the rank of `1`, i.e 1 + 1 = 2.

   Updated arrays:

   ```python
   par = [0, 0, 2, 3, 4, 5]
   rank = [2, 1, 1, 1, 1, 1]
   ```

3. **Union(1, 2)**:

   - `find(1)` returns `0` (following the chain from `1` to `0`).
   - `find(2)` returns `2` (2 is its own parent).
   - Since they are in different subsets, union them:
     - Make `0` the parent of `2`.
     - Update the rank of `0` by adding the rank of `2`, i.e 2 + 1 = 3.

   Updated arrays:

   ```python
   par = [0, 0, 0, 3, 4, 5]
   rank = [3, 1, 1, 1, 1, 1]
   ```

4. **Union(2, 3)**:

   - `find(2)` returns `0` (following the chain from `2` to `0`).
   - `find(3)` returns `3` (3 is its own parent).
   - Since they are in different subsets, union them:
     - Make `0` the parent of `3`.
     - Update the rank of `0` by adding the rank of `3`, i.e 3 + 1 = 4.

   Updated arrays:

   ```python
   par = [0, 0, 0, 0, 4, 5]
   rank = [4, 1, 1, 1, 1, 1]
   ```

5. **Union(4, 5)**:

   - `find(4)` returns `4` (4 is its own parent).
   - `find(5)` returns `5` (5 is its own parent).
   - Since they are in different subsets, union them:
     - Make `4` the parent of `5`.
     - Update the rank of `4` by adding the rank of `5`, i.e 1 + 1 = 2.

   Updated arrays:

   ```python
   par = [0, 0, 0, 0, 4, 4]
   rank = [4, 1, 1, 1, 2, 1]
   ```

## Result

After processing all edges, the union function was executed 4 times, and it returned 1 for each of the 4 executions, indicating that nodes were successfully united into the same set. As a result, the initial value of `res` (which is `n = 6`) is decremented by 1 each time the union function returns 1. After processing all edges, `res` is decremented to 2. This indicates that there are 2 connected components or subsets.

Hence, we have two connected components: `{0, 1, 2, 3}` and `{4, 5}`, so the return value will be `2`. The `par` array indicates the parent of each node, and the `rank` array helps keep the tree balanced.

#### Efficiency Analysis

- **Time Complexity**: $O(E * log N)$

  - In the worst-case scenario, the time complexity of this function is $O(E * log N)$,
  - where:
    - E is the number of edges in the input graph (represented by edges).
    - N is the number of nodes in the graph (represented by n).

- **Space Complexity**: $O(n)$

  - Space is used for the parent and rank arrays, each of size `n`.
