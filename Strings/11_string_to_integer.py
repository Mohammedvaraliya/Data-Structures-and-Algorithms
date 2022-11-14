'''
You are given some numeric string as input. Convert the string you are
given to an integer. Do not make use of the built-in "int" function.
Example:
    "123" : 123
    "-12332" : -12332
    "554" : 554
    etc.
'''

def str_to_int(input_str):
    
    output_int = 0

    if input_str[0] == '-':
        start_idx = 1
        is_negative = True
    else:
        start_idx = 0
        is_negative = False

    for i in range(start_idx, len(input_str)):
        # print(len(input_str))
        # print(i)
        place = 10**(len(input_str) - (i+1))
        digit = ord(input_str[i]) -ord('0')
        output_int += place * digit

    if is_negative:
        return -1 * output_int
    else:
        return output_int

    


if __name__ == "__main__":
    
    str_1 = "123"
    X = str_to_int(str_1)
    print(X)
    print(type(X))
    print("\n")

    str_2 = "-123"
    Y = str_to_int(str_2)
    print(Y)
    print(type(Y))
    print("\n")

    str_3 = "554"
    Z = str_to_int(str_3)
    print(Z)
    print(type(Z))
    print("\n")


