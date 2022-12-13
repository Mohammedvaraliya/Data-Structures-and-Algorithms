def find_sum(n):
    sum = 0

    for i in range(1, n+1):
        print(sum)
        sum += i

    return sum


if __name__ == "__main__":
    print(find_sum(5))