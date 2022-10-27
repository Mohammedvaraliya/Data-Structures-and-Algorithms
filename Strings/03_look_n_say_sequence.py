'''
You have given a string - print the next look-and-say sequence
which means
if you have a string

"111221"
here

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
1211 is read off as "one 1, one 2, then two 1s" or 111221.
111221 is read off as "three 1s, two 2s, then one 1" or 312211.

so the final string will be like this "312211"
'''


def next_number(s):
    result = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i+1]:
            i += 1
            count += 1
        result.append(str(count) + s[i])
        i += 1
    return ''.join(result)

s = "111221"
print(next_number(s))

print("\n")

s1 = "1"
n = 4
for i in range(n):
    s1 = next_number(s1)
    print(s1)
