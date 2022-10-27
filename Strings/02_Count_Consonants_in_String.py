'''
Given a string, count the number of consonants.
Note a consonant is a letter that is not a vowels,
i.e  a letter that is not a,e,i,o, or u. 
'''


vowels = "aeiou"

string_1 = "abc de"
string_2 = "varaliya Mohammed"

def iterative_Count_Consonants(input_string):
    count = 0
    for i in range(len(input_string)):
        if input_string[i].lower() not in vowels and input_string[i].isalpha():
            count += 1
    return count

def recursive_Count_Constant(input_string):

    if input_string == '':
        return 0

    if input_string[0].lower() not in vowels and input_string[0].isalpha():
        return 1 + recursive_Count_Constant(input_string[1:])
    else:
        return recursive_Count_Constant(input_string[1:])


if __name__ == "__main__":
    print(iterative_Count_Consonants(string_1))
    print(iterative_Count_Consonants(string_2))

    print(recursive_Count_Constant(string_1))
    print(recursive_Count_Constant(string_2))

