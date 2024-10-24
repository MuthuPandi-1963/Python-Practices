"""
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and 
choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 
Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

def maxProfit(prices):
    buy=prices[0]
    n=len(prices)
    stock=0
    sell=0
    for i in range(1,n):
        if(buy>prices[i]):
            buy=prices[i]
            stock=buy
        else:
            stock=buy
        j=i
        while(j<n):
            if stock < prices[j]:
                if(sell < prices[j]-stock ):
                    sell=prices[j]-stock
            j+=1
    print(sell)


    

maxProfit([7,1,5,3,6,4])
maxProfit([7,6,4,3,1])
maxProfit([1,2])
maxProfit([2,4,1])