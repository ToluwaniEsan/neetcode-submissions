class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        def robbery(sub_nums):
            if len(nums) <= 2:
                return max(nums)
            sub_rob = [0] * len(sub_nums)

            sub_rob[0] = sub_nums[0]
            sub_rob[1] = max(sub_nums[0], sub_nums[1])

            for i in range(2, len(sub_nums)):
                sub_rob[i] = max(sub_nums[i] + sub_rob[i-2], sub_rob[i-1])

            return sub_rob

        case1 = max(robbery(nums[:-1]))
        case2 = max(robbery(nums[1:]))
        return max(case1, case2)