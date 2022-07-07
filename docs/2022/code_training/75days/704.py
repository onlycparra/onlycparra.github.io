class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l,r = 0,len(nums)-1
        while l+1<r:
            m = l + (r-l) // 2
            if nums[m] <= target:
                l = m
            else:
                r = m
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        return -1
