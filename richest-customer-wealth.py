class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        totals = []
        for pos in accounts:
            totals.append(sum(pos))
        totals.sort(reverse=True)
        return totals[0]
