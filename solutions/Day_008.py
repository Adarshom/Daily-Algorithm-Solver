class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Rotates the array to the right by k steps in-place.
        Uses the reversal method for O(N) time and O(1) space complexity.
        """
        n = len(nums)
        if n == 0:
            return

        # Calculate effective rotations, as k can be larger than n
        k = k % n

        # If k is 0, no rotation is needed
        if k == 0:
            return

        # Helper function to reverse a sub-array
        def reverse(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        # Step 1: Reverse the entire array
        # Example: [1,2,3,4,5,6,7] -> [7,6,5,4,3,2,1]
        reverse(nums, 0, n - 1)

        # Step 2: Reverse the first k elements
        # Example (k=3): [7,6,5,4,3,2,1] -> [5,6,7,4,3,2,1]
        reverse(nums, 0, k - 1)

        # Step 3: Reverse the remaining n-k elements
        # Example: [5,6,7,4,3,2,1] -> [5,6,7,1,2,3,4]
        reverse(nums, k, n - 1)

if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    k1 = 3
    sol.rotate(nums1, k1)
    print(f"Input: [1,2,3,4,5,6,7], k=3 -> Output: {nums1} (Expected: [5,6,7,1,2,3,4])")

    # Test Case 2
    nums2 = [-1, -100, 3, 99]
    k2 = 2
    sol.rotate(nums2, k2)
    print(f"Input: [-1,-100,3,99], k=2 -> Output: {nums2} (Expected: [3,99,-1,-100])")

    # Test Case 3 (k > n)
    nums3 = [1, 2]
    k3 = 3
    sol.rotate(nums3, k3)
    print(f"Input: [1,2], k=3 -> Output: {nums3} (Expected: [2,1])")

    # Test Case 4 (empty array)
    nums4 = []
    k4 = 5
    sol.rotate(nums4, k4)
    print(f"Input: [], k=5 -> Output: {nums4} (Expected: [])")

    # Test Case 5 (single element array)
    nums5 = [42]
    k5 = 10
    sol.rotate(nums5, k5)
    print(f"Input: [42], k=10 -> Output: {nums5} (Expected: [42])")
