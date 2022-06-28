class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            raise Exception("The list 'nums' is empty")
        '''
        dict with pairs (<number previously found>, <index of that number>)
        for every number X in nums[], we will lookup this dictionary first to see
        whether we have seen the value (target-X) before.
        '''
        wanted = {}
        for j in range(len(nums)):
            looking_for = target - nums[j]
            if looking_for in wanted:
                return(wanted[looking_for],j)
            wanted[nums[j]] = j
        raise Exception("No pair found, you lied to me...")
        return
