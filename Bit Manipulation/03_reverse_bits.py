class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
        
        return res






if __name__ == "__main__":

    obj = Solution()

    n1 = 43261596
    print(obj.reverseBits(n=n1))

    n2 = 4294967293
    print(obj.reverseBits(n=n2))