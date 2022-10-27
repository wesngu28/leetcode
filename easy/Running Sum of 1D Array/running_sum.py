class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        for idx,num in enumerate(nums):
            sum = sum + num
            nums[idx] = sum
        return nums

# Am I allowed to mutate the original array?

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        runningSums = []
        for idx,num in enumerate(nums):
            sum = sum + num
            runningSums.append(sum)
        return runningSums

# If they say no