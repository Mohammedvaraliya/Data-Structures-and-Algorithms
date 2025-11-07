class Solution:
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return abs(a)
    
    def gcd_of_array(self, arr):
        if not arr:      
            return 0
        result = arr[0]
        for num in arr[1:]:
            result = self.gcd(result, num)
        return result
    
    def gcd_of_array_smallest_and_largest(self, nums) -> int:
        if not nums:
            return 0
        
        smallest = min(nums)
        largest = max(nums)
        return self.gcd(smallest, largest)
   
    def pairwise_gcd(self, arr):
        n = len(arr)
        result = []
        for i in range(n):
            for j in range(i + 1, n):
                result.append(((arr[i], arr[j]), self.gcd(arr[i], arr[j])))
        return result

    # Infinite generator — note: no 'self' because it doesn't depend on the class
    @staticmethod
    def infinite_numbers(start=12, step=6):
        i = start
        while True:
            yield i
            i += step

    # Optional: compute GCD for first N numbers of infinite generator
    def gcd_stream(self, generator, limit=10):
        result = next(generator)
        count = 1
        for num in generator:
            result = self.gcd(result, num)
            count += 1
            if count >= limit:
                break
        return result


if __name__ == "__main__":
    solution = Solution()

    # Example 1: GCD of two numbers
    print("GCD(48, 18):", solution.gcd(48, 18))

    # Example 2: GCD of an array
    nums = [12, 18, 24]
    print("Array:", nums)
    print("GCD of array:", solution.gcd_of_array(nums))

    print("GCD of array smallest and larget:", solution.gcd_of_array_smallest_and_largest(nums))

    # Example 3: Pairwise GCDs
    pairs = solution.pairwise_gcd(nums)
    print("\nPairwise GCDs:")
    for pair, value in pairs:
        print(f"GCD{pair} = {value}")

    # Example 4: Infinite generator demo (first 10 numbers)
    print("\nGCD of first 10 numbers from infinite generator:")
    gen = Solution.infinite_numbers()
    print(solution.gcd_stream(gen, limit=10))
