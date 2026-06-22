class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s) 
        count = {}
        res = 0
        left = 0
        for right in range (n):
            count[s[right]] = count.get(s[right], 0 ) + 1

            while (right-left+1) - max(count.values()) > k:
                count[s[left]] -= 1 
                left += 1

            res = max(res,right-left+1)
        return res