import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            res[tuple(count)].append(s)
        
        return list(res.values())

        



if __name__ == "__main__":

    obj = Solution()

    str1 = ["eat","tea","tan","ate","nat","bat"]
    print(obj.groupAnagrams(str1))

    str2 = [""]
    print(obj.groupAnagrams(str2))

    str3 = ["a"]
    print(obj.groupAnagrams(str3))