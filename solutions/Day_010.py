import collections
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Use collections.Counter to store frequencies of elements in the first array.
        # This allows for O(1) average time complexity for lookups and updates.
        counts = collections.Counter(nums1)
        
        result = []
        
        # Iterate through the second array.
        for num in nums2:
            # If the current number exists in the counts map and its count is greater than 0,
            # it means we found an intersection for this number.
            if counts[num] > 0:
                result.append(num)  # Add the number to the result list.
                counts[num] -= 1    # Decrement its count as we've used one instance.
                
        return result

if __name__ == "__main__":
    solver = Solution()

    # Test Case 1: Basic intersection
    nums1_1 = [1, 2, 2, 1]
    nums2_1 = [2, 2]
    expected_1 = [2, 2] # Order might vary, but elements and counts should match
    result_1 = solver.intersect(nums1_1, nums2_1)
    print(f"Input: nums1={nums1_1}, nums2={nums2_1}")
    print(f"Output: {result_1}, Expected: {expected_1}")
    # Sort for comparison as order doesn't strictly matter for the problem
    assert sorted(result_1) == sorted(expected_1), f"Test Case 1 Failed: {result_1}"
    print("-" * 30)

    # Test Case 2: Different order and more elements
    nums1_2 = [4, 9, 5]
    nums2_2 = [9, 4, 9, 8, 4]
    expected_2 = [9, 4] # Or [4, 9] or [4, 9] etc.
    result_2 = solver.intersect(nums1_2, nums2_2)
    print(f"Input: nums1={nums1_2}, nums2={nums2_2}")
    print(f"Output: {result_2}, Expected: {expected_2} (or [4,9])")
    assert sorted(result_2) == sorted(expected_2), f"Test Case 2 Failed: {result_2}"
    print("-" * 30)

    # Test Case 3: No common elements
    nums1_3 = [1, 2, 3]
    nums2_3 = [4, 5, 6]
    expected_3 = []
    result_3 = solver.intersect(nums1_3, nums2_3)
    print(f"Input: nums1={nums1_3}, nums2={nums2_3}")
    print(f"Output: {result_3}, Expected: {expected_3}")
    assert sorted(result_3) == sorted(expected_3), f"Test Case 3 Failed: {result_3}"
    print("-" * 30)

    # Test Case 4: One empty array
    nums1_4 = []
    nums2_4 = [1, 2, 3]
    expected_4 = []
    result_4 = solver.intersect(nums1_4, nums2_4)
    print(f"Input: nums1={nums1_4}, nums2={nums2_4}")
    print(f"Output: {result_4}, Expected: {expected_4}")
    assert sorted(result_4) == sorted(expected_4), f"Test Case 4 Failed: {result_4}"
    print("-" * 30)

    print("All test cases passed!")
