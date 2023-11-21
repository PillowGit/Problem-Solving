class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        return (lambda ls:sum(i for i in range(1, len(ls)) if ls[i] != ls[i-1]))(sorted(nums, key=lambda x:-x))