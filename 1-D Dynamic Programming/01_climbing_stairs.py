class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp

        return one




if __name__ == "__main__":

    obj = Solution()

    n1 = 2
    print(obj.climbStairs(n = n1))

    n2 = 3
    print(obj.climbStairs(n = n2))

    n3 = 5
    print(obj.climbStairs(n = n3))