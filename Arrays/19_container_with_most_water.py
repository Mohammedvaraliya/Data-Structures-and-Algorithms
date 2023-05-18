# Brute force
# Time complexity : O(n^2)
def maxArea_method_1(height: list[int]) -> int:
    # Brute force
    res = 0

    for l in range(len(height)):
        for r in range(l + 1, len(height)):
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

    return res

# Time complexity : O(n)
def maxArea_method_2(height: list[int]) -> int:
    res = 0
    l, r = 0, len(height) - 1

    while l < r:
        area = (r - l) * min(height[l], height[r])
        res = max(res, area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    
    return res



if __name__ == "__main__":

    X = [1,8,6,2,5,4,8,3,7]
    print(maxArea_method_1(X))
    print(maxArea_method_2(X))

    Y = [1,1]
    print(maxArea_method_1(Y))
    print(maxArea_method_2(Y))