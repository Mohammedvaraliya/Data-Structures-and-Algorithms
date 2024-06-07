# Data-Structures And Algorithms

### 01. Implement Trie (Prefix Tree)

[Leetcode Problem URL](https://leetcode.com/problems/implement-trie-prefix-tree/description/)

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

- `Trie()` Initializes the trie object.
- `def insert(word: str)` Inserts the string `word` into the trie.
- `def search(word: str) -> bool` Returns `true` if the string `word` is in the trie (i.e., was inserted before), and `false` otherwise.
- `def startsWith(prefix: str) -> bool` Returns `true` if there is a previously inserted string `word` that has the prefix `prefix`, and `false` otherwise.

```bash
Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
```

```
obj = Trie()
word1 = 'apple'
obj.insert(word1)
print(obj.search(word1)) # True
word2 = 'app'
print(obj.search(word2)) # False because the word "app" is not present in the Trie object
prefix = 'app'
print(obj.startsWith(prefix)) # True because the previously inserted string `word` has the prefix `prefix`
obj.insert(word2)
print(obj.search(word2)) # True because the word "app" has been inserted in the Trie object
```

**Explaination**

#### TrieNode Class

The `TrieNode` class represents each node in the Trie. Each node contains:

- A dictionary `children` to store the children nodes.
- A boolean `endOfWord` to indicate if the node marks the end of a word.

#### Trie Class

The `Trie` class manages the TrieNode and implements the three methods `insert`, `search`, and `startsWith`.

1. **Initialization**

```python
class Trie:
    def __init__(self):
        self.root = TrieNode()
```

2. **Insert Method**

The `insert` method adds a word to the Trie. Starting from the root, it iterates through each character in the word. If a character is not already a child of the current node, it creates a new `TrieNode`. After processing all characters, it marks the last node's `endOfWord` as `True`.

3. **Search Method**

The `search` method checks if a word is in the Trie. Starting from the root, it iterates through each character in the word. If a character is not found in the current node's children, it returns `False`. If all characters are found, it returns `True` only if the last node's `endOfWord` is `True`.

4. **StartsWith Method**

The `startsWith` method checks if there is any word in the Trie that starts with the given prefix. It follows a similar process to the `search` method but returns `True` as soon as all characters in the prefix are found.

#### Efficiency Analysis

- **Insert Method:**

  - **Time Complexity:** $(O(n))$, where $(n)$ is the length of the word. This is because each character of the word is processed once.
  - **Space Complexity:** $(O(n))$ in the worst case, where each character in the word requires a new `TrieNode`.

- **Search Method:**

  - **Time Complexity:** $(O(n))$, where $(n)$ is the length of the word. Each character is checked once.
  - **Space Complexity:** $(O(1))$, as no additional space is needed beyond the input word.

- **StartsWith Method:**
  - **Time Complexity:** $(O(m))$, where $(m)$ is the length of the prefix. Each character in the prefix is checked once.
  - **Space Complexity:** $(O(1))$, similar to the `search` method.

#### Explanation

1. **Insertion of "apple":**

   - Traverse through each character in "apple" and create new `TrieNode` for each character.
   - Mark the last node (representing 'e') with `endOfWord = True`.

2. **Search for "apple":**

   - Traverse through each character in "apple".
   - Since all characters are found and the last node has `endOfWord = True`, return `True`.

3. **Search for "app":**

   - Traverse through each character in "app".
   - The last node (representing 'p') does not have `endOfWord = True`, so return `False`.

4. **StartsWith "app":**

   - Traverse through each character in "app".
   - Since all characters are found, return `True`.

5. **Insertion of "app":**

   - Traverse through each character in "app" and use existing nodes.
   - Mark the last node (representing 'p') with `endOfWord = True`.

6. **Search for "app" again:**
   - Traverse through each character in "app".
   - Since all characters are found and the last node has `endOfWord = True`, return `True`.
