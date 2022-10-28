class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for i,piv in enumerate(nums):
            right_sum = total - left_sum - piv
            if left_sum == right_sum:
                return i
            left_sum += piv
        return -1
