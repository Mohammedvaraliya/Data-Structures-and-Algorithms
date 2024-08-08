# Advanced Graphs Data-Structures and Algorithms

## 01. Alien Dictionary

[Leetcode Problem URL](https://leetcode.com/problems/alien-dictionary/description/)
[Lintcode Problem URL](https://www.lintcode.com/problem/892/)

There is a foreign language which uses the latin alphabet, but the order among letters is not `"a", "b", "c" ... "z"` as in English.

You receive a list of non-empty strings `words` from the dictionary, where the words are sorted lexicographically based on the rules of this new language.

Derive the order of letters in this language. If the order is invalid, return an empty string. If there are multiple valid order of letters, return any of them.

A string `a` is lexicographically smaller than a string `b` if either of the following is true:

The first letter where they differ is smaller in `a` than in `b`.
There is no index `i` such that `a[i] != b[i]` and `a.length < b.length`.

The letters in one string are of the same rank by default and are sorted in Human dictionary order

```bash
Example 1:

Input：["wrt","wrf","er","ett","rftt"]
Output："wertf"
Explanation：
from "wrt"and"wrf" ,we can get 't'<'f'
from "wrt"and"er" ,we can get 'w'<'e'
from "er"and"ett" ,we can get 'r'<'t'
from "ett"and"rftt" ,we can get 'e'<'r'
So return "wertf"
```

```bash
Example 2:

Input：["z","x"]
Output："zx"
Explanation：
from "z" and "x"，we can get 'z' < 'x'
So return "zx"
```

```bash
Example 3:

Input: ["z","o"]
Output: "zo"
Explanation:
from "z" and "o", we can get 'z' < 'o'
So return "zo".
```

```bash
Example 4:

Input: ["hrn","hrf","er","enn","rfnn"]
Output: "hernf"
Explanation:
from "hrn" and "hrf", we can get 'n' < 'f'
from "hrf" and "er", we can get 'h' < 'e'
from "er" and "enn", we can get get 'r' < 'n'
from "enn" and "rfnn" we can get 'e'<'r'
so one possible solution is "hernf"
So return "hernf"
```

### Explanation

To solve this problem, I've used a topological sorting approach. Here’s the detailed step-by-step explanation of the solution:

Topological sorting is a technique used to order the vertices of a directed graph in a linear sequence such that for every directed edge `uv` from vertex `u` to vertex `v`, `u` comes before `v` in the ordering. This is particularly useful for tasks like scheduling, dependency resolution, and understanding hierarchical structures.

1. **Build the Graph**:

   - We start by creating an empty adjacency list `adj` to store the graph. For each character in the words, we initialize an empty set in `adj`.

2. **Create the Edges**:

   - For each pair of adjacent words `w1` and `w2` in the list, we find the first differing character and add a directed edge from the character in `w1` to the character in `w2`.
   - If `w1` is longer than `w2` and is a prefix of `w2`, the order is invalid, and we return an empty string.

3. **Topological Sort Using DFS**:

   - We use a depth-first search (DFS) to perform topological sorting.
   - We maintain a `visit` dictionary to keep track of visiting states: `None` (unvisited), `True` (visiting), and `False` (visited).
   - If we encounter a character that is already being visited (i.e., in the current DFS path), it means there is a cycle, and we return an empty string.
   - We append characters to the `res` list after visiting all their neighbors.

4. **Return the Result**:
   - After completing the DFS for all characters, we reverse the `res` list to get the correct topological order and return it as a string.

#### Example Walkthrough

Let's walk through the example `["wrt", "wrf", "er", "ett", "rftt"]` step by step.

Input:

```bash
words = ["wrt", "wrf", "er", "ett", "rftt"]
```

1. **Initialize the Adjacency List**:

   ```python
   adj = {char: set() for word in words for char in word}
   ```

   This creates a graph where each character in the words has an entry pointing to an empty set.

   ```python
   adj = {
       'w': set(),
       'r': set(),
       't': set(),
       'f': set(),
       'e': set(),
   }
   ```

2. **Create Edges Based on Lexicographical Order**:

   Compare each pair of adjacent words to determine the order of characters.

   - Compare "wrt" and "wrf":

     - First differing character: `t` vs `f`
     - `t` should come before `f`
     - Update adjacency list:

       ```python
       adj = {
           'w': set(),
           'r': set(),
           't': {'f'},
           'f': set(),
           'e': set(),
       }
       ```

   - Compare "wrf" and "er":

     - First differing character: `w` vs `e`
     - `w` should come before `e`
     - Update adjacency list:

       ```python
       adj = {
           'w': {'e'},
           'r': set(),
           't': {'f'},
           'f': set(),
           'e': set(),
       }
       ```

   - Compare "er" and "ett":

     - First differing character: `r` vs `t`
     - `r` should come before `t`
     - Update adjacency list:

       ```python
       adj = {
           'w': {'e'},
           'r': {'t'},
           't': {'f'},
           'f': set(),
           'e': set(),
       }
       ```

   - Compare "ett" and "rftt":

     - First differing character: `e` vs `r`
     - `e` should come before `r`
     - Update adjacency list:

       ```python
       adj = {
           'w': {'e'},
           'r': {'t'},
           't': {'f'},
           'f': set(),
           'e': {'r'},
       }
       ```

#### DFS Execution:

1. **Initialize**:

   ```python
   visit = {}
   res = []
   ```

2. **Start DFS for each character** (sorted in reverse order):

   ```python
   for char in sorted([c for c in adj.keys()], reverse=True):
       if dfs(char):
           return ""
   ```

   **Characters sorted in reverse order**: ['w', 't', 'r', 'f', 'e']

3. **DFS Traversal**:

   - Start with `char = 'w'`:
     - `dfs('w')`:
       - Mark 'w' as visiting: `visit = {'w': True}`
       - Visit neighbor 'e':
         - `dfs('e')`:
           - Mark 'e' as visiting: `visit = {'w': True, 'e': True}`
           - Visit neighbor 'r':
             - `dfs('r')`:
               - Mark 'r' as visiting: `visit = {'w': True, 'e': True, 'r': True}`
               - Visit neighbor 't':
                 - `dfs('t')`:
                   - Mark 't' as visiting: `visit = {'w': True, 'e': True, 'r': True, 't': True}`
                   - Visit neighbor 'f':
                     - `dfs('f')`:
                       - Mark 'f' as visiting: `visit = {'w': True, 'e': True, 'r': True, 't': True, 'f': True}`
                       - No neighbors to visit
                       - Mark 'f' as visited: `visit = {'w': True, 'e': True, 'r': True, 't': True, 'f': False}`
                       - Append 'f' to result: `res = ['f']`
                       - Return False
                   - Mark 't' as visited: `visit = {'w': True, 'e': True, 'r': True, 't': False, 'f': False}`
                   - Append 't' to result: `res = ['f', 't']`
                   - Return False
               - Mark 'r' as visited: `visit = {'w': True, 'e': True, 'r': False, 't': False, 'f': False}`
               - Append 'r' to result: `res = ['f', 't', 'r']`
               - Return False
           - Mark 'e' as visited: `visit = {'w': True, 'e': False, 'r': False, 't': False, 'f': False}`
           - Append 'e' to result: `res = ['f', 't', 'r', 'e']`
           - Return False
       - Mark 'w' as visited: `visit = {'w': False, 'e': False, 'r': False, 't': False, 'f': False}`
       - Append 'w' to result: `res = ['f', 't', 'r', 'e', 'w']`
       - Return False
   - Remaining characters 't', 'r', 'f', 'e' are already visited.

4. **Result Construction**:

   - Reverse the result list:
     - `res.reverse()`
     - `res = ['w', 'e', 'r', 't', 'f']`
   - Join the result list to form the string:
     - `return "".join(res)`
     - Output: `"wertf"`

#### Efficiency Analysis

- **Time Complexity**: $O(C + V)$, where $C$ is the total length of all words and $V$ is the number of unique characters.
- **Space Complexity**: $O(C + V)$ for storing the graph and the visiting states.
