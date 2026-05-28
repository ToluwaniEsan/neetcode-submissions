class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #finding two numbers that sum up to a target and returning their indices.
        #Rule: The first number must be smaller than the second number.

        left = 0
        right = len(numbers) - 1

        while left < right:
            summ = numbers[left] + numbers[right]

            if summ < target:
                left += 1
            elif summ > target:
                right -= 1
            else:
                return [left + 1, right + 1]

