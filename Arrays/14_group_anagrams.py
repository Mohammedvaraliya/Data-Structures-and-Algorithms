import collections

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    res = collections.defaultdict(list) #mapping charCount to list of Anagrams

    for s in strs:
        count = [0] * 26 # a...z

        for c in s:
            count[ord(c) - ord('a')] += 1

        res[tuple(count)].append(s)
    
    return res.values()



if __name__ == "__main__":

    str1 = ["eat","tea","tan","ate","nat","bat"]
    str2 = [""]
    str3 = ["a"]
    
    X = groupAnagrams(str1)
    print(X)
    
    Y = groupAnagrams(str2)
    print(Y)
    
    Z = groupAnagrams(str3)
    print(Z)