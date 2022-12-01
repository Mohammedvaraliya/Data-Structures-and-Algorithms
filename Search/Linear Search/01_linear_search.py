def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            print(f"At index Number :",i)
            return True

    return False



if __name__ == "__main__":
    data = [2,4,5,6,7,8,55,65,76,86,90,89,90,111,209,879]
    target = 879

    print(linear_search(data, target))