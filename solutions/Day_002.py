import collections
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # The core idea is to use a hash set (Python's set) to keep track of seen numbers.
        # If we encounter a number that is already in the set, it means it's a duplicate.
        
        # A more Pythonic and concise way is to compare the length of the original list
        # with the length of a set created from the list.
        # A set only stores unique elements. If the lengths are different, it implies
        # that some elements were duplicates and thus removed when converting to a set.
        
        # Convert the list to a set to get only unique elements.
        unique_nums = set(nums)
        
        # If the length of the original list is not equal to the length of the set,
        # it means there were duplicate elements in the original list.
        return len(nums) != len(unique_nums)

# Small test block
if __name__ == "__main__":
    solver = Solution()

    # Test case 1: Contains duplicates
    nums1 = [1, 2, 3, 1]
    print(f"Input: {nums1}, Contains Duplicate: {solver.containsDuplicate(nums1)}") # Expected: True

    # Test case 2: No duplicates
    nums2 = [1, 2, 3, 4]
    print(f"Input: {nums2}, Contains Duplicate: {solver.containsDuplicate(nums2)}") # Expected: False

    # Test case 3: Multiple duplicates
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(f"Input: {nums3}, Contains Duplicate: {solver.containsDuplicate(nums3)}") # Expected: True

    # Test case 4: Empty list
    nums4 = []
    print(f"Input: {nums4}, Contains Duplicate: {solver.containsDuplicate(nums4)}") # Expected: False

    # Test case 5: Single element list
    nums5 = [7]
    print(f"Input: {nums5}, Contains Duplicate: {solver.containsDuplicate(nums5)}") # Expected: False
