'''
Problem:
    Given an array of numbers consisting of daily stock prices, calculate the maximum amount of profit that can be made from buying on one day and selling on another day.

    We consider two approaches to this problem. In the first, we consider a brute force approach that solves the problem in O(N^2), where N is the size of the array of numbers. We then improve upon this solution to take our solution to a time complexity of O(N).
'''


# Time Complexity : O(n^2)
# Space Complexity : O(1)
def buy_and_sell_once_meth1(array):
    max_profit = 0
    buy = 0
    sell = 0
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[j] - array[i] > max_profit:
                max_profit = array[j] - array[i]
    return max_profit


# Time Complexity : O(n)
# Space Complexity : O(1)
def buy_and_sell_once_meth2(array):
    max_profit = 0
    min_price = array[0]

    for price in array:
        min_price = min(min_price, price)

        compare_profit = price - min_price

        max_profit = max(max_profit, compare_profit)

    return max_profit




if __name__ == "__main__":

    
    A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
    
    X = buy_and_sell_once_meth1(A)
    print(X)
    print("\n")

    Y = buy_and_sell_once_meth2(A)
    print(Y)


