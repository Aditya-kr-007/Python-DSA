from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n=len(prices)
        for i in range(n-1):
            if prices[i+1] > prices[i]:
                profit = profit + (prices[i+1] - prices[i])
        return profit
n=int(input("enter the list size= "))
nums=list(map(int,input().split()))
print("the profit is ",Solution().maxProfit(nums))
                