import functools

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """
        Iterative solution using Kadane's Algorithm.
        Finds the maximum sum of a contiguous subarray.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Initialize current_max to store the maximum sum ending at the current position.
        # Initialize global_max to store the overall maximum sum found so far.
        # Both are initialized with the first element, as a single element is a valid subarray.
        current_max = nums[0]
        global_max = nums[0]

        # Iterate through the array starting from the second element.
        for i in range(1, len(nums)):
            # For each element, decide whether to extend the previous subarray
            # or start a new subarray from the current element.
            # current_max = max(current_element, current_element + sum_ending_at_previous)
            # If nums[i] is greater than current_max + nums[i], it means
            # the previous subarray sum (current_max) was negative or too small,
            # so it's better to start a new subarray from nums[i].
            current_max = max(nums[i], current_max + nums[i])

            # Update the global maximum sum found so far.
            global_max = max(global_max, current_max)

        return global_max

    def maxSubArray_recursive(self, nums: list[int]) -> int:
        """
        Recursive solution using Dynamic Programming with Memoization.
        Finds the maximum sum of a contiguous subarray.
        This approach directly translates the DP state definition.
        Time Complexity: O(n) due to memoization
        Space Complexity: O(n) for recursion stack and memoization cache
        """
        n = len(nums)
        
        # Use functools.lru_cache for memoization to optimize recursive calls.
        # dp(i) calculates the maximum subarray sum ENDING at index i.
        @functools.lru_cache(None)
        def dp(i: int) -> int:
            # Base case: The maximum sum ending at index 0 is just nums[0].
            if i == 0:
                return nums[0]
            
            # Recursive step: The maximum sum ending at index i is either:
            # 1. nums[i] itself (starting a new subarray from this element).
            # 2. nums[i] added to the maximum sum ending at index i-1 (extending the previous subarray).
            return max(nums[i], nums[i] + dp(i - 1))

        # The problem asks for the maximum subarray sum overall, not just the one ending at the last index.
        # So, we need to compute dp(i) for all i from 0 to n-1 and find the maximum among them.
        max_overall_sum = -float('inf') # Initialize with negative infinity to ensure any sum is greater.
        for i in range(n):
            max_overall_sum = max(max_overall_sum, dp(i))
            
        return max_overall_sum

if __name__ == "__main__":
    solver = Solution()

    # Test Case 1: Standard example
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Input: {nums1}")
    print(f"Iterative Max Subarray Sum: {solver.maxSubArray(nums1)}") # Expected: 6 ([4,-1,2,1])
    print(f"Recursive Max Subarray Sum: {solver.maxSubArray_recursive(nums1)}") # Expected: 6
    print("-" * 30)

    # Test Case 2: All positive numbers
    nums2 = [1, 2, 3, 4, 5]
    print(f"Input: {nums2}")
    print(f"Iterative Max Subarray Sum: {solver.maxSubArray(nums2)}") # Expected: 15
    print(f"Recursive Max Subarray Sum: {solver.maxSubArray_recursive(nums2)}") # Expected: 15
    print("-" * 30)

    # Test Case 3: All negative numbers
    nums3 = [-1, -2, -3, -4, -5]
    print(f"Input: {nums3}")
    print(f"Iterative Max Subarray Sum: {solver.maxSubArray(nums3)}") # Expected: -1 ([-1])
    print(f"Recursive Max Subarray Sum: {solver.maxSubArray_recursive(nums3)}") # Expected: -1
    print("-" * 30)

    # Test Case 4: Single element array
    nums4 = [7]
    print(f"Input: {nums4}")
    print(f"Iterative Max Subarray Sum: {solver.maxSubArray(nums4)}") # Expected: 7
    print(f"Recursive Max Subarray Sum: {solver.maxSubArray_recursive(nums4)}") # Expected: 7
    print("-" * 30)
