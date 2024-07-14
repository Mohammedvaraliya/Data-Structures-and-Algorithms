class Solution:
    def alien_order(self, words: list[str]) -> str:
        adj = { char:set() for w in words for char in w }

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visit = {} # False = it is visited, True = it is in the current path
        res = []

        def dfs(char):
            if char in visit:
                return visit[char]
            
            visit[char] = True

            for nei in adj[char]:
                if dfs(nei):
                    return True

            visit[char] = False
            res.append(char)
        
        # for char in adj:
        #     if dfs(char):
        #         return ""
        
        for char in sorted([c for c in adj.keys()], reverse=True):
            if dfs(char):
                return ""

        res.reverse()
        return "".join(res)



if __name__ == "__main__":

    obj = Solution()

    words1 = ["wrt","wrf","er","ett","rftt"]
    print(obj.alien_order(words = words1))

    words2 = ["z","x"]
    print(obj.alien_order(words = words2))

    words3 = ["z","o"]
    print(obj.alien_order(words = words3))

    words4 = ["hrn","hrf","er","enn","rfnn"]
    print(obj.alien_order(words = words4))

    word5 = ["ab","adc"]
    print(obj.alien_order(words = word5))
