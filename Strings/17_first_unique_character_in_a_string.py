def firstUniqChar(s: str) -> int:
    char_counts = {}  

    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i

    return -1




if __name__ == "__main__":

    S1 = "leetcode"
    print(firstUniqChar(S1))

    S2 = "loveleetcode"
    print(firstUniqChar(S2))

    S3 = "aabb"
    print(firstUniqChar(S3))

