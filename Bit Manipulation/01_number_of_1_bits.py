class Solution:
    def hammingWeight_method1(self, n: int) -> int:
        res = 0
        
        while n:
            res += n % 2
            n = n // 2
        
        return res
        
    def hammingWeight_method2(self, n: int) -> int:
        res = 0
        
        while n:
            n &= (n-1)
            res += 1
        
        return res





if __name__ == "__main__":

    obj = Solution()

    n1 = 11
    print(obj.hammingWeight_method1(n=n1))
    print(obj.hammingWeight_method2(n=n1))

    n2 = 128
    print(obj.hammingWeight_method1(n=n2))
    print(obj.hammingWeight_method2(n=n2))

    n3 = 2147483645
    print(obj.hammingWeight_method1(n=n3))
    print(obj.hammingWeight_method2(n=n3))