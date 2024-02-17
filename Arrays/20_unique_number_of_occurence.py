def uniqueOccurrences(arr: list[int]) -> bool:
    hash_set = {}
    
    for i in arr:
        if i in hash_set:
            hash_set[i] += 1
        else:
            hash_set[i] = 1
            
    # Check for uniqueness of occurrences
    occurrences_set = set(hash_set.values())
    return len(occurrences_set) == len(hash_set)

if __name__ == "__main__":
    
    arr1 = [1,2,2,1,1,3]
    print(uniqueOccurrences(arr1))
    
    arr2 = [1,2]
    print(uniqueOccurrences(arr2))
    
    arr3 = [-3,0,1,-3,1,1,1,-3,10,0]
    print(uniqueOccurrences(arr3))
    