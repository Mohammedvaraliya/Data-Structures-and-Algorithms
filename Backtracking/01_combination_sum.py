class Solution:

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)
        return res


if __name__ == "__main__":

    obj = Solution()
    
    candidates1 = [2,3,6,7]
    target1 = 7
    res1 = obj.combinationSum(candidates1, target1)
    print(res1)

    candidates2 = [2,3,5]
    target2 = 8
    res2 = obj.combinationSum(candidates2, target2)
    print(res2)

    candidates3 = [2]
    target3 = 1
    res3 = obj.combinationSum(candidates3, target3)
    print(res3)