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

**Explaination**

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

**Explaination**

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

### Efficiency Analysis

- **Time Complexity**:

  - The grid has `m` rows and `n` columns.
  - Each cell is visited once, and each BFS operation considers up to 4 neighbors per cell.
  - The time complexity is $(O(m \times n))$ because we traverse every cell in the grid once.

- **Space Complexity**:
  - The space complexity is also $(O(m \times n))$ due to the `visit` set and the queue used in BFS, which in the worst case can store all cells in the grid.
  - Additionally, the recursive stack of BFS can go up to the size of the grid in the worst case.
