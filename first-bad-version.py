class Solution:
    def repeatedCharacter(self, s: str) -> str:
        new = ""
        for l in s:
            new += l
            if new.count(l) == 2:
                return l
