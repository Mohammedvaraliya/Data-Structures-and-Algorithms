# Strings Data-Structures and Algorithms

## 01. Reverse String

    Reverse String
    To reverse a string using stack operations - push() and pop()

    Example:
            s = "1234567890"

    Traverse the string and push() all the char one by one to the stack till s will empty.
    And
    pop() all the char from stack, so we get our reversed string

         "0987654321"

---

---

## 02. Count Consonants in String

    Count Consonants in String

    Given a string, count the number of consonants.
    Note a consonant is a letter that is not a vowels,
    i.e  a letter that is not a,e,i,o, or u.

    Example:
            string_2 = "varaliya Mohammed"

        Output:
                9

        Because there is 9 char present in the string which is consonent.

            string_2 = "abc de"

        Output:
                3

        Because there is 3 char present in the string which is consonent.

---

---

## 03. Look-and-Say Sequence

    Look-and-Say Sequence

    You have given a string - print the next look-and-say sequence
    which means
    if you have a string

    "111221"
    here

    1 is read off as "one 1" or 11.
    11 is read off as "two 1s" or 21.
    21 is read off as "one 2, then one 1" or 1211.
    1211 is read off as "one 1, one 2, then two 1s" or 111221.
    111221 is read off as "three 1s, two 2s, then one 1" or 312211.

    so the final string will be like this "312211"

---

---

## 04. String Processing: Spreadsheet Encoding

    String Processing: Spreadsheet Encoding

    ord("A") will return The ACII value which is 65
    similarly
    ord("B") is 67

---

---

## 05. String Processing: Is Palindrome

[Leetcode Problem URL](https://leetcode.com/problems/valid-palindrome/)

```bash
String Processing: Is Palindrome

A palindrome is a word or phrase that is the same forward and backwards.
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

s = "Was it a cat I saw?"  # This is true
b = "Testing"              # This is false

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

---

---

## 06. String Processing: Is Anagram

[Leetcode Problem URL](https://leetcode.com/problems/valid-anagram/)

```bash
String Processing: Is Anagram

Anagram is a word or phrase that is made by arranging the letters of another word or phrase in a different order

Example:
        below = elbow.
        study = dusty.
        night = thing.

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false
```

### Explanation

---

---

## 07. String Processing: Is Palindrome Permutation

    String Processing: Is Palindrome Permutation

    Given a String, write a function to check if it is a permutation of a palindrome.

    A palindrome is a word or phrase that is the same forward and backwards.

    A permutation is a rearrangement of a letters. The palindrome does not need
    to be limited to just dictionary words.

    Example:
            palin_perm = "Tact Coa" #Taco Cat
            not_palin_perm = "This is not a palindrome permutation"

---

---

## 08. String Processing: Check Permutation

    String Processing: Check Permutation

    Given two strings, write a method to decide if
    one is a prmutation of the other.

    Example:
            permutation example:
                                is_permutation_1 = "God"
                                is_permutation_2 = "dog"

            no-permutation example:
                                not_permutation_1 = "Not"
                                not_permutation_2 = "got"

---

---

## 09. String Processing: Is Unique

    String Processing: Is Unique

    Implement an algorithm to determine if a string
    has all unique characters.
    Example:
                unique_str_1 = 'ABCdefg'
                non_unique_str_1 = 'non unique STR'

---

---

## 10. String Processing: Integer to String

    String Processing: Integer to String

    You are given some integer as input, (i.e. ... -3, -2, -1, 0, 1, 2, 3 ...)
    Convert the integer you are given to a string.
    Do not make use of the built-in "str" function.

    Examples:

        Input: 123
        Output: "123"

        Input: -123
        Output: "-123"

---

---

## 11. String Processing: String to Integer

[Leetcode Problem URL](https://leetcode.com/problems/string-to-integer-atoi/)

```bash
String Processing: String to Integer

You are given some numeric string as input. Convert the string you are
given to an integer. Do not make use of the built-in "int" function.

Example:
    "123" : 123

    "-12332" : -12332

    "554" : 554

    etc.

ord('0') = 48

ord('1') = 49
we want an integer 1 from given str '1', so

ord('1') - ord('0') = 1

like other integers,
ord('2') - ord('0') = 2
ord('3') - ord('0') = 3
ord('4') - ord('0') = 4

hence, we get our integers

String Processing: String to Integer (atoi)

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.


Note:
    Only the space character ' ' is considered a whitespace character.
    Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.


Example 1:
    Input: s = "42"
    Output: 42
    Explanation: The underlined characters are what is read in, the caret is the current reader position.
    Step 1: "42" (no characters read because there is no leading whitespace)
            ^
    Step 2: "42" (no characters read because there is neither a '-' nor '+')
            ^
    Step 3: "42" ("42" is read in)
            ^
    The parsed integer is 42.
    Since 42 is in the range [-231, 231 - 1], the final result is 42.

Example 2:
    Input: s = "   -42"
    Output: -42
    Explanation:
    Step 1: "   -42" (leading whitespace is read and ignored)
                ^
    Step 2: "   -42" ('-' is read, so the result should be negative)
                ^
    Step 3: "   -42" ("42" is read in)
                ^
    The parsed integer is -42.
    Since -42 is in the range [-231, 231 - 1], the final result is -42.

Example 3:
    Input: s = "4193 with words"
    Output: 4193
    Explanation:
    Step 1: "4193 with words" (no characters read because there is no leading whitespace)
            ^
    Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
            ^
    Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
                ^
    The parsed integer is 4193.
    Since 4193 is in the range [-231, 231 - 1], the final result is 4193.
```

---

---

## 12. Longest Substring Without Repeating Characters

[Leetcode Problem URL](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

Longest Substring Without Repeating Characters

Given a string `s`, find the length of the longest substring without repeating characters.

```bash
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

```bash
Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

```bash
Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

### Explanation

Here, we will use the **Sliding Window** technique with a hash map (dictionary) to keep track of the characters and their latest indices.

#### Approach Explanation

1. Why this approach?

   We need to **track the longest substring without repeating characters**. A brute force solution would try all substrings, check for duplicates, and compute the longest — but that is inefficient (`O(n²)` or worse).

   Instead, we use a **Sliding Window** approach with a **hash map** to efficiently keep track of seen characters.

2. Problem-Solving Pattern

   This problem follows the **Sliding Window** + **Hash Map** pattern:

   - A **sliding window** (`start` to `i`) maintains the current substring without duplicates.
   - A **hash map (dictionary)** stores the latest index of each character.
   - When a duplicate is found, the `start` pointer is adjusted to ensure uniqueness.

3. Why is it efficient?

   - Each character is visited at most **twice** (once by `i`, once by `start` adjustment).
   - Time complexity reduces to **O(n)**.
   - Memory is efficient since we only store characters of the current window.

#### Step-by-Step Walkthrough

1. We will use the example:

   ```bash
   s = "abcabcbb"
   ```

   ```bash
   map = {}       # Stores the last index where each character was seen
   start = 0      # Start index of the current substring window
   max_length = 0 # Keeps track of the max length found
   ```

   | Step | i (index) | s\[i] (char) | Map (char → index) | start | max_length | Action Taken                       |
   | ---- | --------- | ------------ | ------------------ | ----- | ---------- | ---------------------------------- |
   | 1    | 0         | a            | {}                 | 0     | 0          | Add 'a'. max_length = 1            |
   | 2    | 1         | b            | {a:0}              | 0     | 1          | Add 'b'. max_length = 2            |
   | 3    | 2         | c            | {a:0, b:1}         | 0     | 2          | Add 'c'. max_length = 3            |
   | 4    | 3         | a            | {a:0, b:1, c:2}    | 0 → 1 | 3          | 'a' is duplicate → move start to 1 |
   | 5    | 4         | b            | {a:3, b:1, c:2}    | 1 → 2 | 3          | 'b' is duplicate → move start to 2 |
   | 6    | 5         | c            | {a:3, b:4, c:2}    | 2 → 3 | 3          | 'c' is duplicate → move start to 3 |
   | 7    | 6         | b            | {a:3, b:5, c:2}    | 3 → 5 | 3          | 'b' duplicate → move start to 5    |
   | 8    | 7         | b            | {a:3, b:6, c:5}    | 5 → 7 | 3          | 'b' duplicate → move start to 7    |

2. **Final Result:**
   The longest substring without repeating characters is `"abc"`, with length **3**.

#### Time and Space Complexity Analysis

| Complexity Type | Complexity       | Explanation                                                                                                                                          |
| --------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Time**        | **O(n)**         | Each character is processed at most twice (once by `i`, once by `start` adjustment).                                                                 |
| **Space**       | **O(min(n, k))** | Hash map stores characters in the current window. At most `k` unique characters, where `k` is charset size (e.g., 26 for lowercase English letters). |

---

---

## 13. Encode and Decode Strings

[Leetcode Problem URL](https://leetcode.com/problems/encode-and-decode-strings/)

```bash
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode

Example

Example1:
    Input: ["Hello","everyone","have","a", "great", "day"]
    Output: ["Hello","everyone","have","a", "great", "day"]
    Explanation:
    One possible encode method is: "5#Hello8#everyone4#have1#a5#great3#day"

Example2:
    Input: ["we", "say", ":", "yes"]
    Output: ["we", "say", ":", "yes"]
    Explanation:
    One possible encode method is: "2#we3#say1#:3#yes"
```

### Explanation

We use **length-prefixed encoding** to serialize the list of strings into a single string. The format is:

```
<length>#<string>
```

We repeat this format for each string in the list. The `#` serves as a delimiter between the length and the actual string. During decoding, we simply parse the length, extract that many characters, and repeat until the string ends.

#### Encode Method

We loop through each string in the list:

1. Calculate the **length** of the string.
2. Concatenate the length, the `#` delimiter, and the string itself.
3. Append the result to the encoded string.

#### Decode Method

We use a two-pointer approach:

1. Start at the beginning of the string.
2. Move a pointer `j` forward until it finds `#`. The substring from `i` to `j` is the **length** of the next string.
3. Convert this substring into an integer.
4. Extract the next `length` characters and append them to the result.
5. Move the pointer `i` forward to the start of the next encoded segment.
6. Repeat until the end of the encoded string.

#### Detailed Example Walkthrough

1. Let's walk through the full encoding and decoding for this input:

   ```python
   Input: ["Hello", "everyone", "have", "a", "great", "day"]
   ```

2. #### Encoding

3. Initialize: `res = ""`

   | Iteration | String     | Length | Encoded Part | res So Far                               |
   | --------- | ---------- | ------ | ------------ | ---------------------------------------- |
   | 1         | "Hello"    | 5      | "5#Hello"    | "5#Hello"                                |
   | 2         | "everyone" | 8      | "8#everyone" | "5#Hello8#everyone"                      |
   | 3         | "have"     | 4      | "4#have"     | "5#Hello8#everyone4#have"                |
   | 4         | "a"        | 1      | "1#a"        | "5#Hello8#everyone4#have1#a"             |
   | 5         | "great"    | 5      | "5#great"    | "5#Hello8#everyone4#have1#a5#great"      |
   | 6         | "day"      | 3      | "3#day"      | "5#Hello8#everyone4#have1#a5#great3#day" |

4. **Final Encoded String:**

   ```python
   "5#Hello8#everyone4#have1#a5#great3#day"
   ```

5. #### Decoding

6. Now decode `"5#Hello8#everyone4#have1#a5#great3#day"` step by step.

7. Initialize: `res = []`, `i = 0`

   | Iteration | `i` | `j` (where `s[j] == '#'`) | Length | Substring Extracted | New `i` | res                                                 |
   | --------- | --- | ------------------------- | ------ | ------------------- | ------- | --------------------------------------------------- |
   | 1         | 0   | 1                         | 5      | "Hello"             | 7       | \["Hello"]                                          |
   | 2         | 7   | 8                         | 8      | "everyone"          | 17      | \["Hello", "everyone"]                              |
   | 3         | 17  | 18                        | 4      | "have"              | 23      | \["Hello", "everyone", "have"]                      |
   | 4         | 23  | 24                        | 1      | "a"                 | 26      | \["Hello", "everyone", "have", "a"]                 |
   | 5         | 26  | 27                        | 5      | "great"             | 33      | \["Hello", "everyone", "have", "a", "great"]        |
   | 6         | 33  | 34                        | 3      | "day"               | 38      | \["Hello", "everyone", "have", "a", "great", "day"] |

8. **Final Decoded Output:**

   ```python
   ["Hello", "everyone", "have", "a", "great", "day"]
   ```

#### Time and Space Complexity

| Operation | Time Complexity | Space Complexity | Notes                                 |
| --------- | --------------- | ---------------- | ------------------------------------- |
| Encoding  | $O(n $\*$ k)$   | $O(1)$           | n = number of strings, k = avg length |
| Decoding  | $O(n $\*$ k)$   | $O(n)$           | Stores each string in result list     |

---

#### Why This Approach?

- Using length-prefixed encoding (`len#string`) solves issues where strings may contain special characters like `#`, `,`, etc.
- This method is **safe**, **reversible**, and **efficient**.
- It avoids ambiguity during decoding by clearly separating length and content.

Other approaches like delimiter-only (`|`, `,`) or using escape characters can lead to bugs if those characters appear inside the original strings.

---

---

## 14. Longest Repeating Character Replacement

[Leetcode Problem URL](https://leetcode.com/problems/longest-repeating-character-replacement/)

```bash
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achive this answer too.
```

---

---

## 15. Minimum Window Substring

[Leetcode Problem URL](https://leetcode.com/problems/minimum-window-substring/)

```bash
Given two strings s and t of lengths m and n respectively, return the minimum window
substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
```

---

---

## 16. First Letter to Appear Twice

[Leetcode Problem URL](https://leetcode.com/problems/first-letter-to-appear-twice/)

```bash
Given a string s consisting of lowercase English letters, return the first letter to appear twice.

Note:

1. A letter a appears twice before another letter b if the second occurrence of a is before the second occurrence of b.
2. s will contain at least one letter that appears twice.

Example 1:
Input: s = "abccbaacz"
Output: "c"
Explanation:
The letter 'a' appears on the indexes 0, 5 and 6.
The letter 'b' appears on the indexes 1 and 4.
The letter 'c' appears on the indexes 2, 3 and 7.
The letter 'z' appears on the index 8.
The letter 'c' is the first letter to appear twice, because out of all the letters the index of its second occurrence is the smallest.

Example 2:
Input: s = "abcdd"
Output: "d"
Explanation:
The only letter that appears twice is 'd' so we return 'd'.
```

## 17. First Unique Character in a String

[Leetcode Problem URL](https://leetcode.com/problems/first-unique-character-in-a-string/)

```bash
Given a string s, find the first non-repeating character in it and return its index.
If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1
```

---

---

## 18. Find the Index of the First Occurrence in a String

[LeetCode Problem URL](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

```bash
Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
```

```bash
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
```

### Explanation

#### Approach Explanation

1. Why This Approach?

   This problem is a **classic substring search**. Instead of relying on Python’s built-in string methods like `str.find()`, we manually implement the logic to understand how pattern matching works at a fundamental level.

   The approach follows the **brute-force pattern-matching** algorithm but is optimized with early exits and substring comparisons, making it intuitive and educational.

2. Problem-Solving Pattern Used

   - **Sliding Window**: A fixed-size window of the length of `needle` is moved over `haystack` to check for matches.
   - **Brute Force Matching**: We iterate through each starting index and check character-by-character if a match exists.
   - **Greedy Comparison**: We stop at the first successful match without further checking.

3. Why This Is Efficient for the Problem

   - The substring is always compared starting from the left to right.
   - Once a match fails, we immediately shift the window to the next index.
   - This is the most direct and readable approach before applying more advanced algorithms like **KMP (Knuth-Morris-Pratt)** for larger datasets or competitive scenarios.

### Step-by-Step Walkthrough

1. Let’s analyze the behavior of the second method: `strStr(haystack, needle)`

2. Input:

   ```python
   haystack = "sadbutsad"
   needle = "sad"
   ```

   - `len(needle) = 3`
   - We will check substrings of length 3 in `haystack` starting from each index.

3. Iteration Details:

   | i   | haystack\[i\:i+len(needle)] | Comparison     | Match?                                   |
   | --- | --------------------------- | -------------- | ---------------------------------------- |
   | 0   | "sad"                       | "sad" == "sad" | ✅ Yes — return 0                        |
   | 1   | "adb"                       | "adb" == "sad" | ❌ No                                    |
   | 2   | "dbu"                       | "dbu" == "sad" | ❌ No                                    |
   | 3   | "but"                       | "but" == "sad" | ❌ No                                    |
   | 4   | "uts"                       | "uts" == "sad" | ❌ No                                    |
   | 5   | "tsa"                       | "tsa" == "sad" | ❌ No                                    |
   | 6   | "sad"                       | "sad" == "sad" | ✅ Yes — but already returned at index 0 |

   > Since we are looking for the first occurrence, we return 0 immediately, So it won't check the other chars.

4. Final Output:

   ```python
   Return value: 0
   ```

---

#### Time and Space Complexity Analysis

| Metric               | Complexity | Explanation                                                                                                   |
| -------------------- | ---------- | ------------------------------------------------------------------------------------------------------------- |
| **Time Complexity**  | $O(n * m)$ | In the worst case, for each of the `n` characters in `haystack`, we compare up to `m` characters in `needle`. |
| **Space Complexity** | $O(1)$     | No extra space used except for a few variables. No additional data structures are used.                       |

> Note: The slicing operation `haystack[i:i+len(needle)]` takes O(m) time internally, so time complexity remains O(n \* m).

#### Summary

- The solution uses a **sliding window** strategy with a substring match to find the first occurrence.
- It is optimal and simple for most real-world input sizes.
- For large-scale or performance-critical applications, consider using more advanced algorithms like **KMP** or **Rabin-Karp**.

---

---

## 19. Shuffle String

[Leetcode Problem URL](https://leetcode.com/problems/shuffle-string/)

You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.

![Example1](https://assets.leetcode.com/uploads/2020/07/09/q1.jpg)

```bash
Example 1:

Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
c -> 4
o -> 5
d -> 6
e -> 7
l -> 0
e -> 2
e -> 1
t -> 3

Final string = "leetcode"
```

```bash
Example 2:

Input: s = "abc", indices = [0,1,2]
Output: "abc"
Explanation: After shuffling, each character remains in its position.
```

### Explanation

**Approach: Index Mapping with Extra List**

- We initialize an array of empty strings of the same length as `s`.
- For each character in the string `s`, place it at the position given by `indices[i]` in the new array.
- Finally, join the characters of this new array to get the result.

This approach works in **linear time** and uses an auxiliary array to store characters in their new positions.

#### Step-by-Step Walkthrough (Example: `s = "codeleet", indices = [4,5,6,7,0,2,1,3]`)

1. We create an empty list:

   ```
   shuffled_chars = ["", "", "", "", "", "", "", ""]
   ```

2. Now we iterate:

   | Iteration (i) | s\[i] | indices\[i] | Operation              | shuffled_chars                             |
   | ------------- | ----- | ----------- | ---------------------- | ------------------------------------------ |
   | 0             | c     | 4           | Place `'c'` at index 4 | `["", "", "", "", "c", "", "", ""]`        |
   | 1             | o     | 5           | Place `'o'` at index 5 | `["", "", "", "", "c", "o", "", ""]`       |
   | 2             | d     | 6           | Place `'d'` at index 6 | `["", "", "", "", "c", "o", "d", ""]`      |
   | 3             | e     | 7           | Place `'e'` at index 7 | `["", "", "", "", "c", "o", "d", "e"]`     |
   | 4             | l     | 0           | Place `'l'` at index 0 | `["l", "", "", "", "c", "o", "d", "e"]`    |
   | 5             | e     | 2           | Place `'e'` at index 2 | `["l", "", "e", "", "c", "o", "d", "e"]`   |
   | 6             | e     | 1           | Place `'e'` at index 1 | `["l", "e", "e", "", "c", "o", "d", "e"]`  |
   | 7             | t     | 3           | Place `'t'` at index 3 | `["l", "e", "e", "t", "c", "o", "d", "e"]` |

3. Final Result:

   ```python
   "".join(shuffled_chars) → "leetcode"
   ```

#### Time and Space Complexity

| Metric           | Value    | Explanation                                |
| ---------------- | -------- | ------------------------------------------ |
| Time Complexity  | **O(n)** | One pass over the input string and indices |
| Space Complexity | **O(n)** | Extra array `shuffled_chars` of size n     |

#### Why This Approach?

- The problem requires placing characters into known positions — this is a direct use case of **index mapping**.
- Using an extra list allows us to directly assign characters with **O(1)** operations.
- Much more **efficient and cleaner** than building the string character-by-character or doing multiple passes.

#### Pattern Recognition

This problem follows a common **Index Mapping + Output Array** pattern:

- Given elements and their final positions, use a temporary structure to arrange them.
- Appears in problems like:

  - Restoring permutations
  - Reordering arrays based on rules
  - Position-based encoding/decoding

When to apply this:

- Whenever a list of elements and their target indices are given.
- Ideal when constraints allow extra space (`O(n)`).

---

---

## 20. Rotate String

[Leetcode Problem URL](https://leetcode.com/problems/rotate-string/)

Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.

```bash
Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
```

```bash
Example 2:

Input: s = "abcde", goal = "abced"
Output: false
```

### Explanation

**Approach Used: Brute-Force Rotation Check (Custom Rotation)**

- First, check if the lengths of `s` and `goal` are not equal. If not, return `False` immediately.
- Loop through each index from `0` to `len(s) - 1`, and at each index:

  - Rotate the string `s` by slicing: from that index to the end, then concatenate the start to that index.
  - Check if the rotated string matches `goal`.

- If any such rotated string matches, return `True`.
- If no match is found in all possible rotations, return `False`.

#### Step-by-Step Walkthrough

1. Let’s walk through the following example step by step:

   ```python
   s = "abcde"
   goal = "cdeab"
   ```

2. Initial Check:

   `len(s) == len(goal)` → both are 5 characters long.

   | Iteration | i   | Rotation (s\[i:] + s\[:i]) | Is Equal to `goal`? |
   | --------- | --- | -------------------------- | ------------------- |
   | 0         | 0   | "abcde"                    | No                  |
   | 1         | 1   | "bcdea"                    | No                  |
   | 2         | 2   | "cdeab"                    | Yes → Return True   |
   | -         | -   | loop stops                 | -                   |

   → Output: `True`

#### Time and Space Complexity

| Complexity       | Value | Explanation                                                                  |
| ---------------- | ----- | ---------------------------------------------------------------------------- |
| Time Complexity  | O(n²) | There are `n` rotations, each takes up to O(n) time due to slicing + compare |
| Space Complexity | O(n)  | Each rotation creates a new string of size `n`                               |

#### Optimized Observation (Second Method in the code)

Instead of checking all possible rotations, we can observe:
If `goal` is a **rotation** of `s`, then it must be a **substring** of `s + s`.

So an alternate approach would be:

```python
def rotateString(self, s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False

    doubled = s + s

    return goal in doubled
```

| Complexity           | Value    | Explanation                                                                                                                                                                                                      |
| -------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Time Complexity**  | **O(n)** | Concatenating `s + s` takes O(n), and checking if `goal` is a substring of it (`goal in doubled`) takes O(n) using efficient substring search algorithms (like KMP or Boyer-Moore in Python's C implementation). |
| **Space Complexity** | **O(n)** | `s + s` creates a new string of length `2n`, which takes O(n) space. No other data structures are used.                                                                                                          |

#### Pattern Recognition

This is a classic **rotation pattern** where:

- You simulate all possible **shifts** or **rotations**.
- The logic often involves **string slicing** or **concatenation**.
- Can be solved more efficiently using **string doubling** technique (`s + s`).
- Cyclic permutations or circular behavior.

---

---

```

```
