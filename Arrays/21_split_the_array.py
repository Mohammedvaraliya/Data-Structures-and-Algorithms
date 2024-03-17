def isPossibleToSplit(nums: list[int]) -> bool: 
    counter = {}
    
    for num in nums:
        if num in counter:
            counter[num] += 1
            if counter[num] > 2:
                return False
        else:
            counter[num] = 1
    
    return True

if __name__ == "__main__":
    
    nums = [1,1,2,2,3,4]
    print(isPossibleToSplit(nums))
    