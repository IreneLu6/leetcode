def permute(self, nums: List[int]) -> List[List[int]]:
    def backtrack(nums: List[int], index: int, result: List[List[int]], len: int):
        if index == len:
            result.append(nums[:])
            return
        for i in range(index, len):
            nums[index], nums[i] = nums[i], nums[index]
            backtrack(index + 1)
            nums[i], nums[index] = nums[index], nums[i]

    res=[[]]
    backtrack(nums,0,res,len(nums))
    return res