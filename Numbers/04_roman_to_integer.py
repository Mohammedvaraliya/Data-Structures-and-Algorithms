class Solution:
    def romanToInt_method1(self, s: str) -> int:
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
        total = 0

        for i in range(len(s)):
            curr = dict[s[i]]

            if curr > prev:
                total += curr - 2 * prev
                
            else:
                total += curr
            prev = curr

        return total
    
    def romanToInt_method2(self, s: str) -> int:
        roman_map = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100,
            'D': 500, 'M': 1000
        }

        total = 0
        prev_value = 0

        for char in reversed(s):
            value = roman_map[char]

            if value < prev_value:
                total -= value
            else:
                total += value

            prev_value = value

        return total



if __name__ == "__main__":

    obj = Solution()
     
    X = obj.romanToInt_method1("III")
    print(X) # 3

    Y = obj.romanToInt_method1("LVIII")
    print(Y) # 58

    Z = obj.romanToInt_method1("MCMXCIV")
    print(Z) # 1994