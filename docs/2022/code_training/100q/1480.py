from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = []
        if not nums:
            raise Exception("nums is null or empty")
        
        answer.append(nums[0])

        for i in range(1,len(nums)):
            answer.append(nums[i]+answer[i-1])

        return answer
    
