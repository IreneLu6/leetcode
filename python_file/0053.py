from typing import List
import sys

def maxSubArray(self, nums: List[int]) -> int:
    sum, max_sum = 0, -sys.maxsize - 1
    num_len = len(nums)
    for i in range(num_len):
        sum += nums[i]
        max_sum = max(max_sum, sum)
        if sum <= 0 and i != num_len - 1:
            sum = 0
    return max_sum