# Advanced Graphs Data-Structures and Algorithms

### 01. Alien Dictionary

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

**Explanation**
