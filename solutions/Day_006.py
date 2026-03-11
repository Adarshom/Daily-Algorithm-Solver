class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Calculates the maximum profit that can be achieved by buying and selling stocks
        multiple times. You can complete as many transactions as you like.

        The strategy is to sum up all positive differences between consecutive days.
        This greedy approach works because if the price increases from day i to day i+1,
        we can make a profit by buying on day i and selling on day i+1.
        If there's a longer increasing trend (e.g., A < B < C), buying at A and selling at C
        yields profit (C - A). This is equivalent to (B - A) + (C - B), which is
        buying at A, selling at B, then buying at B, selling at C.
        Since we can make unlimited transactions, we simply capture every upward movement.
        """
        max_profit = 0  # Initialize total profit
        
        # Iterate from the second day to the end
        for i in range(1, len(prices)):
            # If the current day's price is higher than the previous day's price
            if prices[i] > prices[i-1]:
                # Add the profit from this single transaction to the total
                max_profit += prices[i] - prices[i-1]
                
        return max_profit

if __name__ == "__main__":
    solver = Solution()

    # Test Case 1: Example from LeetCode
    prices1 = [7, 1, 5, 3, 6, 4]
    expected1 = 7  # (5-1) + (6-3) = 4 + 3 = 7
    result1 = solver.maxProfit(prices1)
    print(f"Prices: {prices1}, Max Profit: {result1}, Expected: {expected1}")
    assert result1 == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {result1}"

    # Test Case 2: Prices are strictly increasing
    prices2 = [1, 2, 3, 4, 5]
    expected2 = 4  # (2-1) + (3-2) + (4-3) + (5-4) = 1 + 1 + 1 + 1 = 4
    result2 = solver.maxProfit(prices2)
    print(f"Prices: {prices2}, Max Profit: {result2}, Expected: {expected2}")
    assert result2 == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {result2}"

    # Test Case 3: Prices are strictly decreasing (no profit)
    prices3 = [7, 6, 4, 3, 1]
    expected3 = 0
    result3 = solver.maxProfit(prices3)
    print(f"Prices: {prices3}, Max Profit: {result3}, Expected: {expected3}")
    assert result3 == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {result3}"

    # Test Case 4: Single element (no transactions possible)
    prices4 = [10]
    expected4 = 0
    result4 = solver.maxProfit(prices4)
    print(f"Prices: {prices4}, Max Profit: {result4}, Expected: {expected4}")
    assert result4 == expected4, f"Test Case 4 Failed: Expected {expected4}, Got {result4}"

    # Test Case 5: Prices with some ups and downs
    prices5 = [1, 7, 2, 3, 6, 7, 6, 7]
    expected5 = 12 # (7-1) + (3-2) + (6-3) + (7-6) + (7-6) = 6 + 1 + 3 + 1 + 1 = 12
    result5 = solver.maxProfit(prices5)
    print(f"Prices: {prices5}, Max Profit: {result5}, Expected: {expected5}")
    assert result5 == expected5, f"Test Case 5 Failed: Expected {expected5}, Got {result5}"

    print("\nAll test cases passed!")
