def findIndexOfFirstOccurence(haystack: str, needle: str) -> int:
    
    n = len(haystack)
    m = len(needle)

    for i in range(n):
        j = 0
        for k in range(i, n):
            if haystack[k] == needle[j]:
                j += 1
            else:
                break
            if j == m:
                return i
            
    return -1
    




if __name__ == "__main__":

    haystack1 = "sabbutsad"
    needle1 = "sad"
    print(findIndexOfFirstOccurence(haystack1, needle1))

    haystack2 = "leetcode"
    needle2 = "leeto"
    print(findIndexOfFirstOccurence(haystack2, needle2))

