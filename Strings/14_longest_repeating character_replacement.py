def characterReplacement(s: str, k: int) -> int:
    count = {}
    res = 0

    l = 0
    maxf = 0

    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])

        while (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1

        res = max(res, r - l + 1)
    
    return res



if __name__ == "__main__":

    X = "ABAB"
    K1 = 2
    print(characterReplacement(X, K1))

    Y = "AABABBA"
    K2 = 1
    print(characterReplacement(Y, K2))

    Z = "ABABBA"
    K3 = 2
    print(characterReplacement(Z, K3))