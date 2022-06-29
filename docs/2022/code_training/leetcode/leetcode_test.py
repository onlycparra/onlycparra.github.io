class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l,r = 0,len(nums)-1
        
        '''while left index is actually at the
        left of the right index'''
        while l+1 < r:
            mid = l + (r-l) // 2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid

        '''what to return if target is:
        - smaller than all
        - in range
        - greater than all'''
        if target < nums[l]:
            return 0
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        if nums[r] < target:
            return r+1

        '''
        l=0
        r=3/ 1
        mid=1
        '''
