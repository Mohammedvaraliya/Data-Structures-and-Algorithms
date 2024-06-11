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
    Mumbai         |         />         \
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

**Explaination**
