class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result=[]
        length = len(nums)
        for i in range(0,length-1):
            for j in range(i+1,length):
                if nums[i]+nums[j] == target:
                    result.append(i)
                    result.append(j)
        return result