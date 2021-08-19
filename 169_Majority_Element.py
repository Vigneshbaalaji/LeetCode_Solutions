from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_major = Counter(nums)
        res = count_major.most_common()[0][0]
        return res