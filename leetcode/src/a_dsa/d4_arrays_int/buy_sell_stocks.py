# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/Most-consistent-ways-of-dealing-with-the-series-of-stock-problems

# LC714. Best Time to Buy and Sell Stock with Transaction Fee
def maxProfit(self, prices: List[int], fee: int) -> int:
    buy_price, profit = inf, 0
    for price in prices:
        buy_price = min(buy_price, price - profit)
        profit = max(profit, price - buy_price - fee)
    return profit

# LC121. Best Time to Buy and Sell Stock
def maxProfit(self, prices: List[int]) -> int:
    t1_cost, t1_profit = float('inf'), 0
    for price in prices:
        # the maximum profit if only one transaction is allowed
        t1_cost = min(t1_cost, price)
        t1_profit = max(t1_profit, price - t1_cost)
    return t1_profit

# LC122. Best Time to Buy and Sell Stock II
def maxProfit2(self, prices: List[int]) -> int:
    if not prices: return 0
    max_p = 0
    # if we have a buy and a sell on same day, just treat they don't happen
    for i in range(1, len(prices)): max_p += max(0, prices[i] - prices[i-1])
    return max_p

# LC123. Best Time to Buy and Sell Stock III
def maxProfit3(self, prices):
    t1_cost, t2_cost = float('inf'), float('inf')
    t1_profit, t2_profit = 0, 0
    for price in prices:
        # the maximum profit if only one transaction is allowed
        t1_cost = min(t1_cost, price)
        t1_profit = max(t1_profit, price - t1_cost)
        # reinvest the gained profit in the second transaction
        t2_cost = min(t2_cost, price - t1_profit)
        t2_profit = max(t2_profit, price - t2_cost)
    return t2_profit

# LC188. Best Time to Buy and Sell Stock IV - You may complete at most k transactions.
def maxProfit4(self, k: int, prices: List[int]) -> int:
    if k == 0: return 0 # check problem 3 for the idea.
    if not prices: return 0
    n = len(prices)
    txa = [[float('inf'), 0] for _ in range(k)]   # cost, profit
    for p in prices:  # O(nk)
        for i in range(k):
            if i == 0:
                txa[i][0] = min(txa[i][0], p)  # cost
                txa[i][1] = max(txa[i][1], p - txa[i][0])  # profit
            else:
                txa[i][0] = min(txa[i][0], p - txa[i-1][1])  # cost
                txa[i][1] = max(txa[i][1], p - txa[i][0])  # profit
    return txa[-1][1]



# return max sum of 2 elements in the array with indices apart from at least k.
# trivial solution takes O(n^2), this takes O(n), one for loop
# https://www.quora.com/Is-it-possible-to-find-maximum-sum-of-two-numbers-in-an-unsorted-array-such-that-the-numbers-are-not-adjacent-to-each-other-in-O-N
# DP is working too: https://www.geeksforgeeks.org/maximum-sum-subsequence-least-k-distant-elements/
def max_sum_k_apart(nums, k):
    if not nums: return 0
    n = len(nums)
    if n <= k: return 0
    emax = nums[0]
    smax = nums[0] + nums[k]
    for i in range(k, n):
        emax = max(emax, nums[i-k])  # track partner's max
        smax = max(smax, emax + nums[i])
    return smax
n = [1, 3, 4, 3, 1, 1, 1]
print(max_sum_k_apart(n, 2))
