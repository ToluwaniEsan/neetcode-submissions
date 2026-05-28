class Solution:
    def rob(self, nums: List[int]) -> int:
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#return the highest number of houses I can rob that I will make the most amount of money from
#With dynamic programming I know one thing I should keep in mind is continuous addition
#I need to add the numbers together, whilst making sure they are not adjacent
#and storing the additions/ possible additions in a list


#tabulation(bottom up)
#dp = [2, 9, 10, 12, 16] -> [2, 9, 8, 3, 6]


        if len(nums) <= 2:
            return max(nums)

        dp = [0] * (len(nums))
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])


        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        return dp[-1]



