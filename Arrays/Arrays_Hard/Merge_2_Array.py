class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #this is a brute force approach ! 
        temp = nums1[:m]
        temp.extend(nums2)
        temp.sort()
        for i in range(m+n):
            nums1[i] = temp[i]