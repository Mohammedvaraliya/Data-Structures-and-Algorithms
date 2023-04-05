def romanToInt(s: str) -> int:
    dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    prev = 0
    curr = 0
    total = 0

    for i in range(len(s)):
        curr = dict[s[i]]

        if curr > prev:
            total += curr - 2 * prev

        else:
            total += curr
        prev = curr

    return total



if __name__ == "__main__":
     
     X = romanToInt("III")
     print(X) # 3

     Y = romanToInt("LVIII")
     print(Y) # 58

     Z = romanToInt("MCMXCIV")
     print(Z) # 1994