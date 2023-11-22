class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        return (lambda d: [v for _,v in sorted(d.items())])({k:v for k,v in [((i+j, j), x) for i in range(len(nums)) for j, x in enumerate(nums[i])]})