def int_to_binary(n):
    result = ""
    power = 1
    while power <= n:
        power *= 2
        
    power //= 2

    while power > 0:
        if power <= n:
            n -= power
            result += "1"
        else:
            result += "0"

        power //= 2

    return result



if __name__ == "__main__":
    a = int_to_binary(10)
    print(a) #1010