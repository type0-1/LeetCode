class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        lsentence = sentence.split()
        for i in range(len(lsentence)):
            pos = lsentence[i]
            if searchWord == pos[0:len(searchWord)]:
                return i + 1
        return -1
