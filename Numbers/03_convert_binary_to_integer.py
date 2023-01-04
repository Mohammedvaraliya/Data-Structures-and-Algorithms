def binary_to_int(binary):
    result = 0
    power = 1
    i = len(binary) - 1
    while i >= 0:
        if binary[i] == "1":
            result += power
        power *= 2
        i -= 1
    return result


if __name__ == "__main__":
    a = binary_to_int("1011")
    print(a) # 11
