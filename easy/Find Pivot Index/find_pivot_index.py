class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum = 0
        for idx, num in enumerate(nums):
            sum = sum + num
        newSum = 0
        for idx, num in enumerate(nums):
            if ((sum-nums[idx]-newSum) == newSum):
                return idx
            newSum += num
        return -1