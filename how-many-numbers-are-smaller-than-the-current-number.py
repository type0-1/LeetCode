class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        big = []
        for n in nums:
            count = 0
            for i in nums:
                if n > i:
                    count += 1
            big.append(count)
        return big
