class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length_of_nums = len(nums)
        LIS = [1] * length_of_nums
        
        for i in range(length_of_nums-1,-1,-1):
            for j in range(i+1,length_of_nums):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1+LIS[j])
                    
        return max(LIS)