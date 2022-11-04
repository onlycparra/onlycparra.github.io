class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums == None or len(nums) == 0:
            return -1

        # check internals by partitioning
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + (r-l)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid
            else: # target > nums[mid]:
                l = mid

        # check edges
        if target == nums[l]:
            return l
        if target == nums[r]:
            return r
        return -1
