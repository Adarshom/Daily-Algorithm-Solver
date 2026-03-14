class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Merges two sorted arrays, nums1 and nums2, into nums1 in-place.
        The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
        To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
        and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
        """
        # Initialize pointers for nums1 (actual elements), nums2, and the write position in nums1.
        # p1 points to the last element of the initial part of nums1.
        p1 = m - 1
        # p2 points to the last element of nums2.
        p2 = n - 1
        # p_write points to the last available position in nums1 (which is m + n - 1).
        p_write = m + n - 1

        # Iterate while there are elements to compare in both arrays.
        # We merge from the end to avoid overwriting elements in nums1 that haven't been processed yet.
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                # If nums1's current element is larger, place it at the current write position.
                nums1[p_write] = nums1[p1]
                p1 -= 1  # Move nums1 pointer backwards.
            else:
                # If nums2's current element is larger or equal, place it.
                nums1[p_write] = nums2[p2]
                p2 -= 1  # Move nums2 pointer backwards.
            p_write -= 1  # Move write pointer backwards.

        # If there are remaining elements in nums2, copy them to the beginning of nums1.
        # This loop is necessary because if all elements of nums1 were larger than remaining nums2 elements,
        # nums2 elements would still need to be placed at the front of nums1.
        # (Elements in nums1 before p1 are already in their correct sorted positions relative to each other
        # and relative to the elements already placed from nums2, so no need to copy nums1's remaining elements.)
        while p2 >= 0:
            nums1[p_write] = nums2[p2]
            p2 -= 1
            p_write -= 1


if __name__ == "__main__":
    solver = Solution()

    # Test Case 1: Standard case (LeetCode example)
    nums1_1 = [1, 2, 3, 0, 0, 0]
    m_1 = 3
    nums2_1 = [2, 5, 6]
    n_1 = 3
    solver.merge(nums1_1, m_1, nums2_1, n_1)
    print(f"Test Case 1: Merged nums1: {nums1_1}")  # Expected: [1, 2, 2, 3, 5, 6]

    # Test Case 2: nums2 is empty (n=0)
    nums1_2 = [1]
    m_2 = 1
    nums2_2 = []
    n_2 = 0
    solver.merge(nums1_2, m_2, nums2_2, n_2)
    print(f"Test Case 2: Merged nums1: {nums1_2}")  # Expected: [1]

    # Test Case 3: nums1 initial part is empty (m=0)
    nums1_3 = [0]
    m_3 = 0
    nums2_3 = [1]
    n_3 = 1
    solver.merge(nums1_3, m_3, nums2_3, n_3)
    print(f"Test Case 3: Merged nums1: {nums1_3}")  # Expected: [1]

    # Test Case 4: nums2 elements are all smaller than nums1 elements
    nums1_4 = [4, 5, 6, 0, 0, 0]
    m_4 = 3
    nums2_4 = [1, 2, 3]
    n_4 = 3
    solver.merge(nums1_4, m_4, nums2_4, n_4)
    print(f"Test Case 4: Merged nums1: {nums1_4}")  # Expected: [1, 2, 3, 4, 5, 6]
