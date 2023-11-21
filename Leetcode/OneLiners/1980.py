class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return list(filter(lambda x:x is not None,(lambda s:[None if i in s else bin(i)[2:].rjust(len(nums), '0') for i in range(len(nums)+1)])(set(int(n,2) for n in nums))))[0]