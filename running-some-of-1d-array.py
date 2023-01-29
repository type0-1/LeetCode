class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        numbers = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            numbers.append(total)
        return numbers
