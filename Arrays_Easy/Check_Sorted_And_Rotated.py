class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        nums2 = nums + nums
        for i in range (n):
            window = nums2[i:i+n]
            if window == sorted(window):
                return True
        return False