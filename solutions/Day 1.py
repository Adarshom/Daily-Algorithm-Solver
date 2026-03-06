class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Create a hash map (dictionary in Python) to store numbers and their indices.
        # The key will be the number, and the value will be its index in the nums array.
        num_map = {}

        # Iterate through the array with both index and value.
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach the target.
            complement = target - num

            # Check if the complement already exists in our hash map.
            # If it does, we've found the two numbers that sum up to the target.
            if complement in num_map:
                # Return the index of the complement (from the map) and the current index i.
                return [num_map[complement], i]
            
            # If the complement is not found, add the current number and its index to the map.
            # This prepares for future iterations where the current number might be a complement.
            num_map[num] = i
        
        # The problem guarantees exactly one solution, so this line should theoretically not be reached.
        # However, it's good practice to have a return statement outside the loop if the problem
        # didn't guarantee a solution or if the loop could finish without finding one.
        return []

if __name__ == "__main__":
    solver = Solution()

    # Test Case 1: Basic example
    nums1 = [2, 7, 11, 15]
    target1 = 9
    # Expected output: [0, 1] because nums[0] + nums[1] == 9
    print(f"Nums: {nums1}, Target: {target1} -> Result: {solver.twoSum(nums1, target1)}")

    # Test Case 2: Different order and values
    nums2 = [3, 2, 4]
    target2 = 6
    # Expected output: [1, 2] because nums[1] + nums[2] == 6
    print(f"Nums: {nums2}, Target: {target2} -> Result: {solver.twoSum(nums2, target2)}")

    # Test Case 3: Numbers with negative values
    nums3 = [-1, -2, -3, -4, -5]
    target3 = -8
    # Expected output: [2, 4] because nums[2] + nums[4] == -3 + -5 == -8
    print(f"Nums: {nums3}, Target: {target3} -> Result: {solver.twoSum(nums3, target3)}")
