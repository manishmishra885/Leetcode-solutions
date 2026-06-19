class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force = generate all poossible substrings 
        # this is the extrerme brute force approach ! 
        '''maxi = 0 
        n = len(s)
        for i in range (n):
            seen = set()
            for j in range (i,n):
                if s[j] in seen:
                    break
                else:
                    seen.add(s[j])
                maxi = max (maxi, j - i + 1) 
        return maxi'''

        maxo = 0 
        left = 0 
        seen = set()
        for right in range (len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1 
            seen.add(s[right])
            maxo = max (maxo, right-left+1)
        return maxo
        