class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        return [(lambda a:all(a[i]*2==a[i-1]+a[i+1] for i in range(1,len(a)-1)))(sorted(nums[i:j+1], key=lambda x:-x)) for i, j in zip(l, r)]