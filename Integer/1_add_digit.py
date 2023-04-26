def addDigits(num: int) -> int:

    digital_root = 0
    while num > 0:
        digital_root += num % 10
        num = num // 10
        
        if num == 0 and digital_root > 9:
            num = digital_root
            digital_root = 0
            
    return digital_root


if __name__ == "__main__":

    num1 = 38
    num2 = 0

    X = addDigits(num1)
    print(X)

    Y = addDigits(num2)
    print(Y)