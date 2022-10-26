class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        rsum = []
        last_sum = 0
        for x in nums:
            last_sum += x
            rsum.append(last_sum)
        return rsum
