def harmonic_sum(n):
    if n < 2:
        return 1
    else:
        return 1/n + (harmonic_sum(n-1))


if __name__ == "__main__":
    
    X = harmonic_sum(10)
    print(X)

    Y = harmonic_sum(7)
    print(Y)