class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Calculates the maximum profit achievable by buying and selling a stock once.

        Args:
            prices: A list of integers where prices[i] is the price of a given stock on the i-th day.

        Returns:
            The maximum profit that can be achieved. If no profit can be made, returns 0.
        """
        # Handle edge case for empty or single-element input array.
        # No transaction can be made, so profit is 0.
        if not prices or len(prices) < 2:
            return 0

        # Initialize min_price to the first day's price.
        # This represents the lowest price encountered so far to buy.
        min_price = prices[0]
        
        # Initialize max_profit to 0.
        # This will store the maximum profit found. If no profit is possible, 0 is returned.
        max_profit = 0

        # Iterate through the prices starting from the second day.
        # We need at least two days to buy and sell.
        for i in range(1, len(prices)):
            current_price = prices[i]
            
            # Update min_price: keep track of the lowest price seen so far.
            # This is the best potential buying point up to the current day.
            min_price = min(min_price, current_price)
            
            # Calculate the potential profit if we sell on the current day.
            # This is current_price - min_price (the lowest price encountered before or on this day).
            potential_profit = current_price - min_price
            
            # Update max_profit: store the maximum profit found among all potential selling days.
            max_profit = max(max_profit, potential_profit)
            
        return max_profit

if __name__ == "__main__":
    solver = Solution()

    # Test case 1: Standard case with clear profit
    prices1 = [7, 1, 5, 3, 6, 4]
    # Expected: Buy at 1 (day 2), Sell at 6 (day 5) -> Profit = 5
    print(f"Prices: {prices1}, Max Profit: {solver.maxProfit(prices1)}") # Expected: 5

    # Test case 2: Prices are always decreasing (no profit possible)
    prices2 = [7, 6, 4, 3, 1]
    # Expected: No profit, return 0
    print(f"Prices: {prices2}, Max Profit: {solver.maxProfit(prices2)}") # Expected: 0

    # Test case 3: Prices are always increasing (profit always possible)
    prices3 = [1, 2, 3, 4, 5]
    # Expected: Buy at 1 (day 1), Sell at 5 (day 5) -> Profit = 4
    print(f"Prices: {prices3}, Max Profit: {solver.maxProfit(prices3)}") # Expected: 4

    # Test case 4: Empty input array
    prices4 = []
    # Expected: 0
    print(f"Prices: {prices4}, Max Profit: {solver.maxProfit(prices4)}") # Expected: 0

    # Test case 5: Single element array
    prices5 = [10]
    # Expected: 0
    print(f"Prices: {prices5}, Max Profit: {solver.maxProfit(prices5)}") # Expected: 0

    # Test case 6: Duplicates and mixed values
    prices6 = [2, 2, 1, 3, 5, 0, 6]
    # Expected: Buy at 0 (day 6), Sell at 6 (day 7) -> Profit = 6
    print(f"Prices: {prices6}, Max Profit: {solver.maxProfit(prices6)}") # Expected: 6
