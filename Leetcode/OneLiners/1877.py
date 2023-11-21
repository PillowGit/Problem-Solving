class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        return max((lambda l:[l[i]+l[-i-1] for i in range(len(nums)//2)])(sorted(nums)))