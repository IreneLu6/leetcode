from typing import List


def threeSum(self, nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()
    for i, num in enumerate(nums):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        tmp = 0 - nums[i]
        while l < r:
            if l > i + 1 and nums[l] == nums[l - 1]:
                l += 1
                continue
            sum = nums[l] + nums[r]

            if sum < tmp:
                l += 1
            elif sum > tmp:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
    return res


nums=[1,-1,-1,0]
threeSum(nums)