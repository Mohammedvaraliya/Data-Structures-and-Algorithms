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
