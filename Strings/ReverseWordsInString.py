class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s.split()
        reverse=temp[::-1]
        result = " ".join(reverse)
        return result