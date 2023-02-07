class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        check = max(candies)
        values = []
        for i in range(len(candies)):
            candies[i] += extraCandies
            if candies[i] >= check:
                values.append(True)
            else:
                values.append(False)
        return values
