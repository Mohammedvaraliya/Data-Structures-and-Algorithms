class Solution:

    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s

        return res


    def decode(self, s: str) -> list[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i : j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length

        return res





if __name__ == "__main__":

    obj = Solution()
    
    X = ["Hello", "everyone", "have", "a", "great", "day"]
    Y = obj.encode(X)
    print(Y)
    print(obj.decode(Y))
    
    print()

    Z = ["we", "say", ":", "yes"]
    A = obj.encode(Z)
    print(A)
    print(obj.decode(A))