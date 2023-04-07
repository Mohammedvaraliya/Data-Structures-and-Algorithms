def containsDuplicate(nums: list[int]) -> bool:
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
          
        hashset.add(n)

    return False




if __name__ == "__main__":

    A = [1,2,3,1]
    B = [1,2,3,4]
    C = [1,1,1,3,3,4,3,2,4,2]

    X = containsDuplicate(A)
    print(X)

    Y = containsDuplicate(B)
    print(Y)

    Z = containsDuplicate(C)
    print(Z)
    