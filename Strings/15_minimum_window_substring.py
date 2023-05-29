def minWindow(s: str, t: str) -> str:
    if t == "":
        return ""
    
    countT, window = {}, {}
    
    for c in t:
        countT[c] = 1 + countT.get(c, 0)

    have, need = 0, len(countT)
    res, resLen = [-1, -1], float("infinity")
    l = 0

    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c, 0)

        if c in countT and window[c] == countT[c]:
            have += 1

        while have == need:
            # Update our results
            if (r - l + 1) < resLen:
                res = [l, r]
                resLen = (r - l + 1)
            
            # Pop from the left of our window
            window[s[l]] -= 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            l += 1

    l, r = res
    return s[l : r + 1] if resLen != float("infinity") else ""






if __name__ == "__main__":

    S1 = "ADOBECODEBANC"
    T1 = "ABC"
    print(minWindow(S1, T1))

    S2 = "a"
    T2 = "a"
    print(minWindow(S2, T2))

    S3 = "a"
    T3 = "aa"
    print(minWindow(S3, T3))