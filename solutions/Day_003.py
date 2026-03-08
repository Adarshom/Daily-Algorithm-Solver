class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        
        # Initialize the answer array.
        # This array will first store the prefix products.
        # answer[i] will eventually hold the product of all elements except nums[i].
        answer = [1] * n
        
        # Step 1: Calculate prefix products
        # answer[i] will store the product of all elements to the left of index i.
        # For index 0, there are no elements to the left, so answer[0] remains 1.
        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]
            
        # Step 2: Calculate suffix products and combine with prefix products
        # Use a variable 'right_product' to keep track of the product of elements
        # to the right of the current index.
        # Initialize right_product to 1 (product of elements to the right of the last element).
        right_product = 1
        
        # Iterate from right to left
        for i in range(n - 1, -1, -1):
            # At this point, answer[i] contains the product of elements to the left of i.
            # Multiply it by right_product (which is the product of elements to the right of i).
            answer[i] = answer[i] * right_product
            
            # Update right_product for the next iteration (moving leftwards).
            # It accumulates the product of elements from the right.
            right_product = right_product * nums[i]
            
        return answer

if __name__ == "__main__":
    solver = Solution()
    
    # Example 1: Basic case with positive integers
    nums1 = [1, 2, 3, 4]
    expected1 = [24, 12, 8, 6]
    result1 = solver.productExceptSelf(nums1)
    print(f"Input: {nums1}, Output: {result1}, Expected: {expected1}")
    assert result1 == expected1, f"Test Case 1 Failed: {result1}"
    
    # Example 2: Case with zeros and negative numbers
    nums2 = [-1, 1, 0, -3, 3]
    expected2 = [0, 0, 9, 0, 0]
    result2 = solver.productExceptSelf(nums2)
    print(f"Input: {nums2}, Output: {result2}, Expected: {expected2}")
    assert result2 == expected2, f"Test Case 2 Failed: {result2}"

    # Example 3: Single element array
    nums3 = [7]
    expected3 = [1]
    result3 = solver.productExceptSelf(nums3)
    print(f"Input: {nums3}, Output: {result3}, Expected: {expected3}")
    assert result3 == expected3, f"Test Case 3 Failed: {result3}"

    print("\nAll test cases passed!")
