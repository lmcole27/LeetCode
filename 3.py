class Solution(object):
  def maxProfit(self, prices):
    """
        :type prices: List[int]
        :rtype: int
        """
    buy = max(prices)
    buy_day = prices.index(buy)
    sell = 0
    max_profit = 0

    for i in range(len(prices)):
      if prices[i] < buy:
        buy = prices[i]
        buy_day = i
        sell = 0
      if i > buy_day:
        if prices[i] > sell:
          sell = prices[i]

        if prices[i] - buy > max_profit:
          max_profit = sell - buy
      
    return max_profit


nums = [3,3,5,0,0,3,1,4]
x = Solution().maxProfit(nums)

print(x)
