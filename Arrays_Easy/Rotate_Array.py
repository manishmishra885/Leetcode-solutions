class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        return (nums)
        # while k > 0:
        #     nums[:] = nums[-1:] + nums[:-1]
        #     k = k-1
        # return nums
        