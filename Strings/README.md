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

    String Processing: Is Palindrome

    A palindrome is a word or phrase that is the same forward and backwards.


    s = "Was it a cat I saw?"  # This is true
    b = "Testing"              # This is false
 
### 06. String Processing: Is Anagram

    String Processing: Is Anagram

    Anagram is a word or phrase that is made by arranging the letters of another word or phrase in a different order

    Example:
            below = elbow.
            study = dusty.
            night = thing.

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

    String Processing: String to Integer

    You are given some numeric string as input. Convert the string you are
    given to an integer. Do not make use of the built-in "int" function.

    Example:
        "123" : 123

        "-12332" : -12332
        
        "554" : 554
        
        etc.

    ord('1') = 49
    we want an integer 1 from given str '1', so

    ord('1') - 48 = 1
    hence, we get our number



