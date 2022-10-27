'''
Implement an algorithm to determine if a string 
has all unique characters.
Example:    unique_str_1 = 'ABCdefg'
            non_unique_str_1 = 'non unique STR'
'''

def normalize(str):
    str = str.replace(" ", "")
    return str.lower()

def is_unique_meth1(str):

    d = dict()
    for i in str:
        if i in d:
            d[i] += 1
            return False
        else:
            d[i] = 1    
    return True

def is_unique_meth2(str):
 
    return len(set(str)) == len(str)

def is_unique_meth3(str):
    
    alpha = "abcdefghijklmnopqrstuvwxyz"

    for i in str:
        if i in alpha:
            alpha = alpha.replace(i, "")
        else:
            return False
    return True
        



if __name__ == "__main__":

    unique_str_1 = 'ABCdefg'
    unique_str_2 = 'HemLo Guys'
    non_unique_str_1 = 'non unique STR'
    non_unique_str_2 = 'hello this is non unique'

    unique_str_1 = normalize(unique_str_1)
    unique_str_2 = normalize(unique_str_2)
    non_unique_str_1 = normalize(non_unique_str_1)
    non_unique_str_2 = normalize(non_unique_str_2)

    print(unique_str_1)
    print(unique_str_2)
    print(non_unique_str_1)
    print(non_unique_str_2)
    print("\n")


    print(is_unique_meth1(unique_str_1))
    print(is_unique_meth1(unique_str_2))
    print(is_unique_meth1(non_unique_str_1))
    print(is_unique_meth1(non_unique_str_2))
    print("\n")

    print(is_unique_meth2(unique_str_1))
    print(is_unique_meth2(unique_str_2))
    print(is_unique_meth2(non_unique_str_1))
    print(is_unique_meth2(non_unique_str_2))
    print("\n")

    print(is_unique_meth3(unique_str_1))
    print(is_unique_meth3(unique_str_2))
    print(is_unique_meth3(non_unique_str_1))
    print(is_unique_meth3(non_unique_str_2))
    print("\n")
