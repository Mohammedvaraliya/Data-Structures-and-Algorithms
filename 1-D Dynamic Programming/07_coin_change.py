class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        result = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        if dp[amount] != amount + 1:
            result = dp[amount]
        else:
            result = -1
        
        return result




if __name__ == "__main__":
    obj = Solution()

    coins1 = [1,2,5]
    amount1 = 11
    print(obj.coinChange(coins = coins1, amount = amount1))

    coins2 = [2]
    amount2 = 3
    print(obj.coinChange(coins = coins2, amount = amount2))

    coins3 = [1]
    amount3 = 0
    print(obj.coinChange(coins = coins3, amount = amount3))
