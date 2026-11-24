class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        buy = prices[0]
        profit = 0
        max_values = len(prices)

        for i in range(1, max_values):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy

        return profit


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7,1,5,3,6,4]))
    print(sol.maxProfit([7,6,4,3,1]))
    print("All tests passed successfully!")