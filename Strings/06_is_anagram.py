# Method-1

s1 = "fairy tales"
s2 = "rail safety"

s1 = s1.replace(" ", "").lower()
s2 = s2.replace(" ", "").lower()

print(s1)
print(s2)

'''
Requires n log n time(since any comparison
based sorting algorithm rquires at least n log n time
to sort)
'''
print(sorted(s1) == sorted(s2))
print("\n")

# Method-2

def is_anagram(s1, s2):
    ht = dict()
    
    if len(s1) != len(s2):
        return False
    
    for i in s1:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1

    for i in s2:
        if i in ht:
            ht[i] -= 1
        else:
            ht[i] = 1

    for i in ht:
        if ht[i] != 0:
            return False
    return True
        

if __name__ == "__main__":

    X = is_anagram(s1, s2)
    print(X)