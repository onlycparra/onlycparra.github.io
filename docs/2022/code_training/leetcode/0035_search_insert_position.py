class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l,r = 0,len(nums)-1

        '''if empty list'''
        if r == -1:
            return 0
        
        '''narrow the search down'''
        while l+1 < r:
            mid = l + (r-l) // 2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid

        print(f'l:{l}\nr:{r}')
        
        '''post-processing'''
        if target <= nums[l]:
            return l
        if target <= nums[r]:
            return r
        else:
            return r+1
