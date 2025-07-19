class Solution:
    def maxProfit_brute_force(self, prices: list[int]) -> int:
        max_profit = 0

        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] > max_profit:
                    max_profit = prices[j] - prices[i]

        return max_profit
    
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min = prices[0]

        for price in prices:
            if price < min:
                min = price

            profit = price - min

            if profit > max_profit:
                max_profit = profit
                
        return max_profit
    
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min = prices[0]

        for price in prices:
            if price < min:
                min = price
            else:
                max_profit = max(max_profit, (price - min))
                
        return max_profit




if __name__ == "__main__":

    obj = Solution()

    
    A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
    B = [7, 1, 5, 3, 6, 4]
    C = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]
    
    print(obj.maxProfit(A))

    print(obj.maxProfit(B))

    print(obj.maxProfit(C))