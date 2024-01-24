def repeatedCharacter(s: str) -> str:
    visited_set = set()

    for i in s:
        if i in visited_set:
            return i
        else:
            visited_set.add(i)






if __name__ == "__main__":

    S1 = "abccbaacz"
    print(repeatedCharacter(S1))

    S2 = "abcdd"
    print(repeatedCharacter(S2))