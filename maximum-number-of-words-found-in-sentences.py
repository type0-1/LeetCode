class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        i = 0
        m = 0
        while i < len(sentences):
            word = sentences[i].strip().split()
            if len(word) > m:
                m = len(word)
            i += 1
        return m
