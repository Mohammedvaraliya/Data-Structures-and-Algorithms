# Data-Structures And Algorithms


### 01. Reverse String

    Reverse String
    To reverse a string using stack operations - push() and pop()

    Example:
            s = "1234567890"
    
    Traverse the string and push() all the char one by one to the stack till s will empty.
    And
    pop() all the char from stack, so we get our reversed string

         "0987654321"
    
### 02. Count Consonants in String

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

### 03. Look-and-Say Sequence

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

### 04. String Processing: Spreadsheet Encoding

    String Processing: Spreadsheet Encoding

    ord("A") will return The ACII value which is 65
    similarly
    ord("B") is 67

### 05. String Processing: Is Palindrome

[Leetcode Solution URL](https://leetcode.com/problems/valid-palindrome/)

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

### 06. String Processing: Is Anagram

[Leetcode Solution URL](https://leetcode.com/problems/valid-anagram/)

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

### 07. String Processing: Is Palindrome Permutation

    String Processing: Is Palindrome Permutation

    Given a String, write a function to check if it is a permutation of a palindrome.

    A palindrome is a word or phrase that is the same forward and backwards.

    A permutation is a rearrangement of a letters. The palindrome does not need
    to be limited to just dictionary words.

    Example:
            palin_perm = "Tact Coa" #Taco Cat
            not_palin_perm = "This is not a palindrome permutation"

### 08. String Processing: Check Permutation

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

### 09. String Processing: Is Unique

    String Processing: Is Unique

    Implement an algorithm to determine if a string 
    has all unique characters.
    Example:    
                unique_str_1 = 'ABCdefg'
                non_unique_str_1 = 'non unique STR'

### 10. String Processing: Integer to String

    String Processing: Integer to String

    You are given some integer as input, (i.e. ... -3, -2, -1, 0, 1, 2, 3 ...)
    Convert the integer you are given to a string. 
    Do not make use of the built-in "str" function.

    Examples:

        Input: 123
        Output: "123"

        Input: -123
        Output: "-123"

### 11. String Processing: String to Integer

[Leetcode Solution URL](https://leetcode.com/problems/string-to-integer-atoi/)

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

### 12. Longest Substring Without Repeating Characters

[Leetcode Solution URL](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

```bash
Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

### 13. Encode and Decode Strings

[Leetcode Solution URL](https://leetcode.com/problems/encode-and-decode-strings/)

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

### 14. Longest Repeating Character Replacement

[Leetcode Solution URL](https://leetcode.com/problems/longest-repeating-character-replacement/)

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