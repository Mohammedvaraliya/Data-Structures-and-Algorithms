def sumDigit(n):
    if n == 0:
        return 0

    else:
        return n % 10 + sumDigit(n//10)



if __name__ == "__main__":
    print(sumDigit(345))