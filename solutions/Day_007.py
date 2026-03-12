from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        Moves all 0's to the end of the array while maintaining the relative order
        of the non-zero elements. This is done using a two-pointer approach.
        """
        # `insert_pos` tracks the position where the next non-zero element should be placed.
        # It effectively marks the boundary between processed non-zero elements
        # (to its left) and elements yet to be processed (at or to its right).
        insert_pos = 0

        # Iterate through the array with a 'read' pointer `i`.
        for i in range(len(nums)):
            # If the element at the current 'read' pointer `i` is non-zero,
            # it means this element needs to be moved to the front of the array.
            if nums[i] != 0:
                # If the 'read' pointer `i` is not the same as the 'insert' pointer,
                # it implies that `nums[insert_pos]` is currently a zero (or an element
                # that has already been processed and will be overwritten).
                # In this case, we swap the non-zero element from `nums[i]` with
                # `nums[insert_pos]`. This moves the non-zero element to its correct
                # position at the front, and effectively places a zero (or an element
                # that will eventually be overwritten by a zero) at position `i`.
                if i != insert_pos:
                    nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
                
                # Increment `insert_pos` to point to the next available slot
                # for a non-zero element.
                insert_pos += 1

if __name__ == "__main__":
    solver = Solution()

    # Test Case 1: Standard case with zeros in various positions
    nums1 = [0, 1, 0, 3, 12]
    solver.moveZeroes(nums1)
    print(f"Input: [0, 1, 0, 3, 12], Output: {nums1}, Expected: [1, 3, 12, 0, 0]")
    assert nums1 == [1, 3, 12, 0, 0]

    # Test Case 2: Array with all zeros
    nums2 = [0, 0, 0]
    solver.moveZeroes(nums2)
    print(f"Input: [0, 0, 0], Output: {nums2}, Expected: [0, 0, 0]")
    assert nums2 == [0, 0, 0]

    # Test Case 3: Array with no zeros
    nums3 = [1, 2, 3]
    solver.moveZeroes(nums3)
    print(f"Input: [1, 2, 3], Output: {nums3}, Expected: [1, 2, 3]")
    assert nums3 == [1, 2, 3]

    print("\nAll test cases passed!")
