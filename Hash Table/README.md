# Hash Table Data-Structures and Algorithms

## 01. Hash Table Implementation

    Hash Table Implementation
    How hash table works

    how list and array different from hash table

## 02. Hash Table Implementation : Get Hash

    Hash Table Implementation : Get Hash

    get hash function returns the integer after converting all the characters to an ASCII value

    Example:
            'vara'

            ord('v') will retun ASCII value of char v

            118 +

            ord('a') will retun ASCII value of char a

            118 + 97 +

            ord('r') will retun ASCII value of char r

            118 + 97 + 114 +

            ord('a') will retun ASCII value of char a

            118 + 97 + 114 + 97

            = 426 % 100

            = 26

            so, when we try to add the value in hash table with index 'vara', it will add to index 9.

## 03. Hash Table Implementation : Collision Handling In Hash Table

    Hash Table Implementation : Collision Handling In Hash Table
    In collision handling the value can be stored in a multiple key value format on the same index number.

    Example:
            get_hash() functions return the hash value of given string

            obj.get_hash("122-Mar") return hash value 82

                it means '122-Mar' is index number 82

            obj.get_hash("1-Mar") return hash value 82

                it means '1-Mar' is index number 82

            Now, Assign values

            obj["122-Mar"] = 550
            obj["1-Mar"] = 220

            if you check the value of obj["122-Mar"], it will return 220, because at the given index number the
            value is overriding

            Hash Table Collision Handling Using Chaining

            using linked list or linear probing

            replace None with empty list

            and if new key come append it on the same index number

            array will look like this

            [[], [], [('1-Mar', 550), ('122-Mar', 120)], [], [], [], [], [], [], []]
