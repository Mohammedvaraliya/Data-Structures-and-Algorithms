'''
Solution uses extra space proportional to size of string "s"
s = ''.join([i for i in s if i.isalnum()]).replace(" ", "").lower()
print(s == s[::-1])

'''

def is_palindrome_method_1(s):
    i = 0
    j = len(s) - 1
    
    while i < j:
        while not s[i].isalnum() and i < j:
            i +=1
        while not s[j].isalnum() and i < j:
            j -= 1

        if s[i].lower() != s[j].lower():
            return False
        
        i += 1
        j -= 1
    return True

def alphaNum(c):
    return (ord('A') <= ord(c) <= ord('Z') or 
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))

def is_palindrome_method_2(s):
    l, r = 0, len(s) - 1

    while l < r:
        while l < r and not alphaNum(s[l]):
            l += 1

        while r > l and not alphaNum(s[r]):
            r -= 1

        if s[l].lower() != s[r].lower():
            return False
        
        l += 1
        r -= 1
    return True



if __name__ == "__main__":

    
    A = "Was it a cat I saw?"  # This is true
    B = "Testing"              # This is false
    C = "A man, a plan, a canal: Panama"

    print(is_palindrome_method_1(A))
    print(is_palindrome_method_1(B))
    print(is_palindrome_method_1(C))
    print("\n")
    print(is_palindrome_method_2(A))
    print(is_palindrome_method_2(B))
    print(is_palindrome_method_2(C))
