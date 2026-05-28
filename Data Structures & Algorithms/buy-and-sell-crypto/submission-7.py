class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #acc, what if i have like a min and max kind of counter and check
        #whether the values at those positions, the buy comes first with the smallest
        #first by saying we pick the middle as the endpoint

        l = 0
        r = 1
        res = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                res = max(res, profit)
            else:
                l = r
            r += 1

        return res


#If the left is bigger than the right or equal to it the left moves forward
#if the right is bigger than the left, after it subtracts it moevs to the right commpulsorily

            