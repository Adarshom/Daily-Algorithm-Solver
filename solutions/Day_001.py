class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Create a hash map to store numbers and their indices.
        # This allows for O(1) average time complexity for lookups.
        num_map = {} 

        # Iterate through the list with both index and value.
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach the target.
            complement = target - num

            # Check if the complement already exists in our hash map.
            if complement in num_map:
                # If it does, we found the two numbers.
                # Return the index of the complement and the current index.
                return [num_map[complement], i]
            
            # If the complement is not found, add the current number and its index to the map.
            # This makes it available as a complement for subsequent numbers.
            num_map[num] = i
        
        # The problem guarantees exactly one solution, so this line should theoretically not be reached.
        return [] 

if __name__ == "__main__":
    solver = Solution()

    # Test Case 1: Basic example
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Nums: {nums1}, Target: {target1} -> Result: {solver.twoSum(nums1, target1)}") # Expected: [0, 1]

    # Test Case 2: Numbers with negative values
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"Nums: {nums2}, Target: {target2} -> Result: {solver.twoSum(nums2, target2)}") # Expected: [1, 2]

    # Test Case 3: Larger numbers and different order
    nums3 = [3, 3]
    target3 = 6
    print(f"Nums: {nums3}, Target: {target3} -> Result: {solver.twoSum(nums3, target3)}") # Expected: [0, 1]
