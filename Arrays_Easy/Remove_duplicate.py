class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = []
        
        for num in nums:
            if num not in unique:
                unique.append(num)
        
        # Copy back into nums (LeetCode requires modifying nums in-place)
        for i in range(len(unique)):
            nums[i] = unique[i]
        
        return len(unique)