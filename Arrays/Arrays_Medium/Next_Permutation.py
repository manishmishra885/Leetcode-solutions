class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # from itertools import permutations

        # all_permu = sorted(list(permutations(nums)))

        # current = all_permu.index(tuple(nums))

        # if current == len(all_permu) - 1:
        #     nums[:] = list(all_permu[0])
        # else:
        #     nums[:] = list(all_permu[current + 1])

        # return nums
        i = len(nums) - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1

            while nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1:] = reversed(nums[i + 1:])