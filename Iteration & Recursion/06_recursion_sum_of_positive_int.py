def sum_series(n):
  if n < 1:
    return 0
  else:
    return n + sum_series(n - 2)


if __name__ == "__main__":

    print(sum_series(6))
    print(sum_series(10))