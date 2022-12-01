def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            print(f"At index Number :",i)
            return True
    return False



if __name__ == "__main__":
    data = [2, 4, 3, 15, 12, 87, 55]
    target = 15

    print(linear_search(data, target))