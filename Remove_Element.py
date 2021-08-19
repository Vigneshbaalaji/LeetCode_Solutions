from collections import Counter
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count_nums = Counter(nums)
        remove_it = count_nums[val]
        for i in range(remove_it):
            nums.remove(val)
        return len(nums)