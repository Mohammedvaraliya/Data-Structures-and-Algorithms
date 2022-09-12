'''
Use a stack data structure to convert integer values to binary.

Example : 242

242 / 2 = 121 -> 0    # 0 is a remainder as number is even
121 / 2 = 60  -> 1    # 1 is a remainder as number is odd
60 / 2  = 30  -> 0    # 0 is a remainder as number is even
30 / 2  = 15  -> 0    # 0 is a remainder as number is even
15 / 2  = 7   -> 1    # 1 is a remainder as number is odd
7 / 2   = 3   -> 1    # 1 is a remainder as number is odd
3 / 2   = 1   -> 1    # 1 is a remainder as number is odd
1 / 2   = 0   -> 1    # 1 is a remainder as number is odd

'''

from stack_DS import Stack

def div_by_2(dec_num):
    s = Stack()

    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num // 2

    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())

    return bin_num



print(div_by_2(242))