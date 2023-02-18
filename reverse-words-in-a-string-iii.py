class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        new = ""
        for word in s:
            new += word[::-1] + " "
        return new.strip()
            
